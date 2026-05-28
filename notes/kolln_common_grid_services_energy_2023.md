# Common Grid Services: Energy Service | Project Pillar: Literature Review
**Date:** May 2026
**Status:** Technical Documentation

## 🎯 Executive Summary
This section of the GMLC report defines the Energy service as the scheduled production or consumption of real power at an electrical location over a committed period. It provides a standardized framework to decouple physical operational objectives (like peak load management) from performance-based service specifications at the transmission and distribution levels.

## 🔑 Key Arguments & Findings
* **Finding 1:** Grid service definitions must focus on the physical and temporal performance parameters required from the provider (e.g., power level and duration) rather than the requestor's internal operational objectives (e.g., peak load management), simplifying scheduling and resource qualification.
* **Finding 2:** Distribution-level energy services are primarily implemented as price-reactive mechanisms (e.g., Time-of-Use or critical-peak pricing) where the exact consumption change is unspecified, contrasting with wholesale markets where blocks of energy are precisely cleared, settled, and subject to non-performance penalties.

## 🛠️ Methodological Notes / Technical Specifications
* **Electrical Attributes:** Power (MW/kW level), Energy (quantity over interval), and Electrical Location (producing/delivering pricing nodes or PNodes).
* **Timing Attributes:** Delivery Schedule (start time and duration/end time) and Delivery Schedule Notification (timing of market clearance).
* **Measurement:** Quantified via revenue-grade interval meters synchronized to the delivery schedule, with potential correction factors applied for physical location discrepancies.

## 💡 Personal Insights & Open Questions
* **Potential Application:** Directly validates EGoT's scheduling architecture. EGoT's End Device (`EDevice`) and Discovery (`DCAP`) microservices map these timing and location attributes using the IEEE 2030.5 XML schema to coordinate battery and load schedules, using Mirror Usage Points (`MUP`) for telemetry and billing verification.
* **Gap/Next Step:** While the report establishes the service taxonomy, it does not address how distribution line constraints (e.g., local voltage rise or thermal overload) should dynamically alter wholesale energy service delivery schedules at the retail-utility boundary.

## 📌 Critical Quotes
> "Scheduling the production and consumption of energy over time allows the system operator to balance energy use with generation to manage delivery limitations caused by power flow constraints as well as stressed periods of operation, such as system peak load management."
---
