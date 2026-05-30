# Dissertation Rewrite Draft: Energy Grid of Things (EGoT) & Energy Service Interface (ESI)

This document contains the expanded ideas, background justifications, architectural mappings, and simulation design details for my dissertation rewrite. It addresses the core elements required for my defense, incorporating the GMLC Common Grid Services definitions and ESI lifecycle mapping.

---

## 1. Introduction

The primary contribution of this dissertation is the formal conceptualization and complete, standard-compliant implementation of the **Energy Service Interface (ESI)**. The ESI is defined by the Grid Modernization Laboratory Consortium (GMLC) as an architectural boundary between customer-owned Distributed Energy Resources (DERs) and utility-side Grid Service Providers (GSPs). Unlike concrete communication protocols, the ESI is a conceptual framework that dictates *how* interactions must be structured to preserve grid stability while protecting consumer boundaries. Because it is not a rigid specification, much of its implementation is left to interpretation. 

This work takes the six common grid services defined by the GMLC (Energy, Reserve, Regulation, Frequency Response, Voltage Management, and Blackstart) and maps them across the five primary phases of the ESI lifecycle:
1. **Registration**: Discovery of capabilities, authentication, and service subscription.
2. **Scheduling**: Negotiation of capacity windows and active power limits.
3. **Operation**: Execution of real-time control actions and telemetry tracking.
4. **Validation**: Performance tracking, error calculation, and conformance verification.
5. **Settlement**: Reconciling performance telemetry against agreements for billing credits.

The secondary contribution is populating this template with an open, widely adopted standard: **IEEE Std 2030.5-2018 (Smart Energy Profile 2.0)**. We demonstrate how standard IEEE 2030.5 resources map directly to all ESI lifecycle phases. A key distinction in our implementation is addressing the client-driven nature of IEEE 2030.5. Unlike legacy SCADA protocols (like Modbus or DNP3) that allow direct utility overrides, IEEE 2030.5 operates as a client-initiated REST API. Utilities cannot push commands directly to devices; instead, clients must poll or subscribe to resources. We analyze how this model alters control latency and modifies client behavior, particularly for customer loads that are typically operated by humans in the loop (e.g., smart thermostats or EV charging).

Finally, we justify the chosen mapping and implementation through a combination of literature citations (for transient and complex dynamic interactions) and active co-simulations using our Go-based EGoT platform coupled with OpenDSS.

---

## 2. Energy Service Interface (ESI) Pillars & Lifecycles

### The Four Pillars of ESI

To construct a robust ESI boundary, we must satisfy the four pillars of ESI:
1. **Privacy**: Personal Private Information (PPI) and high-resolution load profiles must be isolated. In our EGoT platform, this is achieved by separating core end-device registration (`/edev`) from operational data. Each microservice manages its own decoupled SQLite database. Telemetry published to Mirror Usage Points (`/mup`) is stored independently of billing accounts, preventing unauthorized correlation of real-time usage with customer identities.
2. **Trust**: Trust must be established symmetrically. While literature proposes complex behavioral trust scores (e.g., Fernando 2021) based on historical communication reliability, we implement a **direct, performance-based settlement engine**. By comparing Mirror Usage Point telemetry directly against scheduled control targets, the server evaluates compliance objectively. This avoids subjective trust metrics and keeps the system resilient against soft failures (e.g., network packet loss).
3. **Security**: We address cyber-physical risks associated with DER grid services. Security is anchored in transport-layer Mutual TLS (mTLS) with ECDSA P-256 curves, deriving the client's Long-Form Device Identifier (LFDI) from certificate fingerprints. To address the vulnerability of transport-layer security being blind to malicious content (e.g., if utility credentials are compromised and a validly-signed but destructive Volt-Var curve is issued, as shown in Sarker 2020), we define the pathway for an **application-layer check**. Clients must validate incoming curves against local physical safety bounds (e.g., restricting inverter reactive power to $\pm 1.0$ pu and rate-of-change limits) as a local fail-safe.
4. **Interoperability**: Enforced by strict compliance with standard IEEE 2030.5 XML schemas and CSIP (Common Smart Inverter Profile) test procedures. Interoperability is validated through automated type generation from standard WADL files.

### The Five Lifecycles

The data exchange required for grid service participation follows a five-step lifecycle:
- **Registration**: Discovery of root capabilities (`/dcap`), server time synchronization (`/tm` quality = 7), SFDI/LFDI verification, and Function Set Assignment (`/fsa`) mapping.
- **Scheduling**: Negotiation of active/reactive capability windows. IEEE 2030.5 supports this through client-initiated **Flow Reservation Requests** (`/frq`) or server-side scheduled control events.
- **Operation**: Periodically polling for active event states (`/derp/1/actderc` or `/dr/1/actedc`). The client interpolates control setpoints from curves and updates its hardware state.
- **Validation**: Tracking and logging execution. Clients report their execution status (Status = 1 [Received], 2 [Started], 3 [Completed]) via the Response service (`/rsps`) and log alarms (`/edev/{id}/lel`) for fault conditions.
- **Settlement**: Processing compliance. Telemetry posted to Mirror Usage Points (`/mup`) is aggregated, compared against the scheduled targets by the `operator.SettlementEngine`, and applied to `CustomerAccount` credits.

---

## 3. Mapping Common Grid Services to IEEE Std 2030.5

Since IEEE Std 2030.5 does not have explicit, native resources for all six GMLC grid services, we map them to standard resources as follows:

| GMLC Grid Service | IEEE 2030.5 Primary Resource | Transaction Phase & Mapping Rationale |
| :--- | :--- | :--- |
| **Energy Service** | `/frq` & `/frp` | Scheduled active power. Handled via Flow Reservation Requests and Responses, allowing clients to request and servers to allocate power windows. |
| **Reserve Service** | `/derp` (controls & status) | Contingency active power capacity. Mapped using scheduled `DERControl` events that remain inactive until a grid contingency triggers response state reporting (`/rsps`). |
| **Regulation** | `/frq` / `/derp` | Fast active power tracking. Scheduled via Flow Reservation, with active power setpoints updated at 5-minute intervals. Performance is validated using 5-minute average tracking error. |
| **Frequency Response** | `/derp/1/dc` (CurveType = 12) | Autonomous frequency-watt response. Mapped to DER Curves defining frequency-watt active power droop settings, executed locally by the client. |
| **Voltage Management**| `/derp/1/dc` (CurveType = 11) | Reactive power voltage support. Mapped to Volt-Var curves (`CurveType=11`), with telemetry updated to include reactive power (`VARh`) and local voltage (`V`). |
| **Blackstart** | `/dr` & `/derp` | Cold load pickup. Lacking a native blackstart resource, it is mapped to the Demand Response (DR) function set (using `EndDeviceControl` to coordinate sequential reconnection of loads) and DERP for generator frequency support. |

---

## 4. Methods & Architecture

The **EGoT Platform** is structured as a fleet of Go microservices coordinated by an Nginx API Gateway. Each microservice is responsible for a single IEEE 2030.5 resource path (e.g., `/der` or `/mup`), ensuring security boundaries and database isolation.

### decoupled storage and Boilerplate Scaffolding
- **Boilerplate**: Go structs and routing templates are auto-generated from standard WADL schemas using `scaffold-gen` and `wadl-extract`.
- **Database Isolation**: Each service writes to an independent SQLite database using CGO-free drivers. Operational data is serialized using Go's `encoding/gob` to optimize I/O and enforce the privacy boundary between service telemetry and customer accounts.

### OpenDSS Co-Simulation Setup
To evaluate grid-level impacts, we coordinate EGoT device emulators (PV, ESS, EV, controllable loads) with the IEEE 13-Node Test Feeder in OpenDSS:
- Aggregated DER clients are mapped to **Bus 671** at the end of the radial feeder, where voltage sensitivities are highest.
- At each simulation step, the Python co-simulation script (`egot_sim.py`) reads telemetry profiles from EGoT database exports, scales them, updates OpenDSS generator models (`Generator.kW = -P_telemetry / 1000.0`), solves the load flow, and records feeder losses and voltage profiles.

---

## 5. Grid Service Evaluation & Results

### Simulation Scenarios
1. **Scenario 2.1 (EIM & Regulation)**: Models coordinated EV charging and ESS active power dispatch over a 24-hour day. Results demonstrate that coordinating EV charging to align with peak solar generation and using the ESS to buffer imbalances prevents node voltages from falling below the ANSI C84.1 limit (0.95 pu) and reduces line losses by up to 25% compared to the uncoordinated baseline.
2. **Scenario 2.2 (Blackstart Cold Load Pickup)**: Simulates sequential reconnection of 5 load/generation devices. In the uncoordinated baseline, all loads reconnect immediately at step 0, causing a 18kW load spike that exceeds the 12kW transformer capacity and triggers grid collapse. In the coordinated scenario, the ESI uses `EndDeviceControls` to stagger reconnection intervals (12-minute steps), keeping the peak demand below 10kW.
3. **Scenario 2.3 (Reserve Settlement)**: Validates performance-based settlement. The `SettlementEngine` processes simulated Mirror Usage Point telemetry against DER controls, verifying that Device 1 and Device 2 achieved 96.2% and 98.7% tracking accuracy, respectively.

### Communication Overhead (HTTP Metrics)
To address the debate surrounding the computational weight of XML-based REST APIs vs. lightweight IoT protocols (e.g., MQTT), we collect network traffic metrics during our co-simulation runs. We log:
- **Request Count**: Total number of HTTP transactions per lifecycle phase.
- **Data Volume (Bytes)**: Total payload bytes transferred (including headers and XML payloads).
- **Latency (ms)**: Round-trip times for key endpoints like `/derp/1/actderc`.
These metrics highlight that while IEEE 2030.5 XML payloads introduce larger data footprints than binary or JSON protocols, the overhead is highly predictable and manageable for standard utility polling rates (e.g., 15-minute intervals).

### Simplified GMLC Telemetry and Settlement
We justify our telemetry models by defining simplified, practical metrics:
- **Regulation**: Measured as the average root-mean-square error (RMSE) between active power setpoints and MUP telemetry over 5-minute windows, avoiding the overhead of sub-second ISO mileage tracking.
- **Voltage Management**: Reconciles reactive power support (VARh) and local voltages (V) posted to MUP telemetry, validating that the client adhered to the scheduled Volt-Var curve.

---

## 6. Conclusion

The EGoT platform validates that the conceptual Energy Service Interface (ESI) can be fully realized using the IEEE Std 2030.5 protocol. By mapping the GMLC Common Grid Services to standard resources, we provide a blueprint for a standardized, source-agnostic interaction boundary. This standard-compliant ESI protects customer privacy, enforces mTLS-based security, and verifies compliance through performance-based settlement, facilitating the integration of high-penetration DERs into future smart grids.
