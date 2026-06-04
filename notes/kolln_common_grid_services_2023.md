# Common Grid Services: Terms and Definitions Report (PNNL-34483) | Project Pillar: Literature Review

**Report Date:** July 2023  
**Review Date:** May 2026  
**Status:** Technical Literature Notes  
**Authors:** Jaime Kolln, Steve Widergren (PNNL); Jingjing Liu, Rich Brown (LBNL)  
**Report Number:** PNNL-34483

---

## 🎯 Executive Summary
This report establishes a standardized vocabulary and set of definitions for **Common Grid-DER Services** to facilitate cyber-physical transactions across the Energy Services Interface (ESI). It distinguishes the requestor's *operational objectives* (why the service is needed, e.g., peak load management) from the provider's *performance expectations* (what the resource physically delivers at the connection point). It categorizes grid-DER interactions into **six common services** (Energy, Reserve, Regulation, Frequency Response, Voltage Management, and Blackstart), outlining their electrical, timing, and verification attributes for both wholesale bulk markets and distribution retail coordination.

---

## 🔑 Separation of Operational Objectives & Grid Services
* **The Problem:** Traditional utility integrations define services based on grid objectives (e.g., "peak load management," "congestion mitigation"). This is confusing to DER providers and promotes direct control.
* **The Solution:** A grid-DER service is performance-based and specifies *what* to deliver at the point of connection, not *why* or *how*. The same physical service can satisfy multiple operational objectives, preserving privacy and enabling device-agnostic asset participation.

```
┌─────────────────────────────────┐         ┌──────────────────────────────────┐
│ Requestor Operational Objective  │  ───>   │   Performance-Based Grid Service  │
│ (Why/How: Congestion/Peak Mgmt) │         │ (What/When: 10kW load cut, 5-7pm)│
└─────────────────────────────────┘         └──────────────────────────────────┘
```

---

## 📐 Detailed Breakdown of the Six Common Services

### 1. Energy Service
* **Description:** A scheduled active power production or consumption over a committed period.
* **Electrical Attributes:** Power (kW/MW level), Energy quantity (kWh/MWh), and Electrical Location (point of system connection, pricing node/zone). Can be represented as a quantity-price Curve.
* **Timing Attributes:** Start/end time (or start & duration), delivery schedule notification.
* **M&V:** Revenue-grade interval meters matched to schedule intervals. Baselines are established to calculate demand response reductions.

### 2. Reserve Service
* **Description:** Reserves capacity to produce/consume energy when called upon over a committed period.
* **Electrical Attributes:** Reserved power capacity, available reserve energy, electrical location (often defined by zones/areas).
* **Timing Attributes:** Start/end availability, delivery schedule notification, and **Speed of Response** (ramp rate, e.g. time to respond when dispatched).
* **M&V:** Interval metering combined with time-stamped power telemetry during active dispatch events.

### 3. Regulation Service
* **Description:** Continuous real power tracking of rapidly changing signals (every 2-4 seconds) against a basepoint.
* **Electrical Attributes:** Power, Power regulation range, **Power Mileage** (sum of absolute up/down power changes), electrical location.
* **Timing Attributes:** Start/end times, delivery schedule notification, signal periodicity (2-4 seconds), speed of response.
* **M&V:** Sub-second metering reporting real power change in each step. Verified using a **Performance Score** (average correlation, delay, and precision of response against the dispatch signal, e.g., PJM mileage markets).

### 4. Frequency Response Service
* **Description:** Nearly instantaneous, autonomous response to local frequency deviations.
* **Electrical Attributes:** Percent droop, deadband (Hz), electrical location (balancing area).
* **Timing Attributes:** Start/end times of on-call availability, schedule notification.
* **M&V:** Frequency response measurement evaluates initial response (arresting) and sustained response intervals. Verified using a three-step process: **sample validation, response type classification, and droop verification**.

### 5. Voltage Management Service
* **Description:** Voltage support (raise/lower) within specified target ranges over a committed period.
* **Electrical Attributes:** Target voltage/range (kV or RMS range), electrical location.
* **Timing Attributes:** Start/end times, schedule notification, signal periodicity (e.g. 15-minute intervals).
* **M&V:** Verified by metering lagging/leading reactive power (VAR) capability. In distribution, profiling circuit voltage sags/swells (Volt-VAR curves).

### 6. Blackstart Service
* **Description:** Energize or remain available without grid power to restore part of the system.
* **Electrical Attributes:** Real power change, power regulation range, electrical location.
* **Timing Attributes:** Delivery schedule, notification timing, speed of response.
* **M&V:** Compliance tests demonstrating the capability to operate without access to grid power (islanded/grid-forming capability) and interval metering of energy flow.

---

## 🛠️ Performance Determination & Measurement Metrics

The report identifies several technical metrics that are critical to implementing ESI agreements:
1. **Power Mileage:** Replaces simple energy clearing by summing the absolute value of all active power changes ($\sum |P_t - P_{t-1}|$). Used to evaluate battery/storage control effort.
2. **Performance Score Components:**
   * *Correlation:* Phase alignment between regulation signal and output.
   * *Delay:* Propagation time of control action.
   * *Precision:* Scaling accuracy between request and delivery.
3. **Droop Verification:** Autonomous governors must track local grid frequency and adjust power according to:
   $$\Delta P = -\frac{f - f_{nominal}}{f_{nominal} \cdot \text{Droop}}$$

---

## 💡 Connections to EGoT & Dissertation

### 1. Mapping to EGoT Microservices
PNNL-34483 outlines the physical specifications that EGoT's microservices must verify:
* **egot/mup (:8017):** Collects interval meter data for **Energy** services, real power mileage logs for **Regulation**, Volt-VAR telemetry for **Voltage Management**, and sub-second frequency event logs.
* **egot/flowreservation (:8027):** Schedules and reserves capacity for **Reserve** services, maintaining the available energy reserve.
* **egot/derp (:8013):** Distributes parameters for autonomous response curves (deadbands, droop curves, Volt-VAR boundaries).
* **egot/dcap (:8012):** Links electrical locations (pricing nodes, zones, feeders) to resource registrations.

### 2. Implementation Action Items & Research Gaps
Our previous lifecycle review (`notes/grid_services_lifecycle_review.md`) highlighted several gaps between EGoT and GMLC definitions. The terms and definitions in PNNL-34483 provide the physical formulas to resolve these gaps:
* **Regulation Telemetry & Billing:** Update the MUP database schema to calculate the PJM-style **Performance Score** (correlation, delay, precision) and track power mileage during active intervals.
* **Reserve Event Logging:** Implement dispatch telemetry logging, tracking the exact response delay and ramp rate to verify "Speed of Response" against the reserve contract.
* **Voltage Management & Frequency Droop:** Map local voltage and frequency readings to the MUP, enabling post-event droop verification and active reactive power tracking.
* **True Blackstart Restoration:** Rewrite `blackstart.md` in EGoT lifecycles to require GFM (grid-forming) capability validation rather than treating blackstart as a simple demand response program.

---

## 📌 Critical Quotes
> "The grid service is the means to achieve the operational objective. By developing clear, concise, service-oriented, and performance-based grid service definitions, the requested service and the performance expectations are clear to both the provider and the requestor." (Page 1.1)

> "The objective of defining a reserve service is to be agnostic to whether the service is provided by producers or consumers, as long as they meet the performance expectation." (Page 2.8)

> "The ability to closely follow the accuracy of the response can be measured using a metric called 'performance score' or 'performance index,' which is a unit-less quantity between '0' and '1'." (Page 2.9)

> "The reliable provision of the frequency response service must be so quick as to require the active response of resources based on locally measured or sensed changes in frequency, i.e., autonomous response." (Page 2.11)
