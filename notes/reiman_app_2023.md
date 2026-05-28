# App Deconfliction: Orchestrating Distributed, Multi-Agent, Multi-Objective Operations for Power Systems | Project Pillar: Methodology
**Date:** May 2026
**Status:** Peer-Reviewed Literature

## 🎯 Executive Summary
This paper proposes a formalized system architecture and deconfliction pipeline to resolve setpoint conflicts that arise when multiple independent, distributed applications (such as resilience and market-based applications) concurrently attempt to control overlapping sets of grid-edge and IoT devices. The authors demonstrate deconfliction strategies using rules, heuristics, application engagement, and optimization to orchestrate harmonious control behavior.

## 🔑 Key Arguments & Findings
* **Finding 1:** The shift toward active distribution networks with modular, plug-and-play applications (e.g., in ADMS or DERMS platforms) creates a complex control environment where multiple applications can issue contradictory setpoints (e.g., simultaneous battery charge and discharge commands) to overlapping device pools.
* **Finding 2:** Inserting a "Deconfliction Pipeline" between device-controlling applications and protocol converters provides a standardized layer to dynamically frame, solve, and execute resolved control setpoints using rules, heuristics, direct app negotiations, or mathematical optimization.

## 🛠️ Methodological Notes / Technical Specifications
* **Architecture:** Deconfliction Pipeline containing three stages (problem setup, solver execution, action feedback) placed between application logic and device converters (DNP3, Modbus, IEEE 2030.5).
* **Methods Analyzed:** Optimal Power Flow (OPF), Multi-Objective Optimization (MOO) using Pareto-fronts, Multi-Criteria Decision Making (MCDM) using AHP (Analytical Hierarchy Process) or SMARTER, and rule-based heuristics.
* **Testing Bounds:** Demonstrated on a pair of simple greedy applications controlling an ESS.

## 💡 Personal Insights & Open Questions
* **Potential Application:** This architecture is directly relevant to the EGoT platform, where multiple grid services (e.g., Volt-Var curve optimization, Flow Reservation, and demand response controls from DERP) can issue conflicting commands to end devices. Designing a deconfliction pipeline at the Nginx Gateway or within a dedicated coordinator microservice would prevent conflicting emulated device setpoints.
* **Gap/Next Step:** The deconfliction pipeline relies on resolving setpoints before sending them to the device converter. How can this centralized pipeline scale to millions of highly distributed, edge-computing agents operating under communication constraints and varying latencies?

## 📌 Critical Quotes
> "Conflicts can emerge between applications that want to control overlapping sets of device setpoints. We propose a formalized approach to resolving these conflicts that can be applied when integrating new algorithms or developing customized solutions."
> "A Deconfliction Pipeline is inserted between the device-controlling applications and the device protocol converter, which transmits control setpoints from the operations platform to the devices."
