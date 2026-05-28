# Common Grid Services: Reserve Service | Project Pillar: Literature Review
**Date:** May 2026
**Status:** Technical Documentation

## 🎯 Executive Summary
The Reserve service specifies the allocation of a dedicated capacity of real power to be held in reserve and produced or consumed upon request over a committed period. This service provides contingency capacity to handle sudden system disturbances, generator outages, or forecasting errors.

## 🔑 Key Arguments & Findings
* **Finding 1:** Defining a reserve service must be agnostic to whether the service is provided by producers (synchronized/spinning generation) or consumers (demand response curtailment), focusing solely on the ability to meet response time and duration targets.
* **Finding 2:** Distribution-level reserves are increasingly aggregated via curtailment service providers (CSPs) or demand-response programs, which can be dispatched by wholesale markets (e.g., MISO's Demand Response Energy Market) to behave as virtual contingency reserves.

## 🛠️ Methodological Notes / Technical Specifications
* **Electrical Attributes:** Power (level of standby capacity), Energy (amount of energy held in reserve that could be called upon), and Electrical Location (typically defined on a zonal basis).
* **Timing Attributes:** Delivery Schedule (availability window), Delivery Schedule Notification (publication timing), and Speed of Response (the time to ramp to the requested output, e.g., 10 minutes or 30 minutes).
* **Measurement:** Reserve compliance is quantified by combining energy interval metering with time-stamped power measurements to verify the speed and sustainability of the response.

## 💡 Personal Insights & Open Questions
* **Potential Application:** Directly applies to the `FlowReservation` microservice in the EGoT platform, which coordinates reservation requests. Understanding that reserve definitions must remain source-agnostic helps EGoT treat battery storage systems (ESS) and smart loads (HVAC) symmetrically during contingency events.
* **Gap/Next Step:** The report does not discuss the impact of local distribution grid topology (e.g., phase imbalance or transformer limits) when an aggregator dispatches spatially distributed retail assets to meet a bulk grid reserve instruction.

## 📌 Critical Quotes
> "The objective of defining a reserve service is to be agnostic to whether the service is provided by producers or consumers, as long as they meet the performance expectation."
---
