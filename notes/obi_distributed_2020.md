# Distributed energy resource aggregation using customer-owned equipment: A review of literature and standards | Project Pillar: Literature Review
**Date:** May 2026
**Status:** Peer-Reviewed Literature

## 🎯 Executive Summary
This review paper analyzes how aggregations of residential-scale Distributed Energy Resources (DERs)—such as water heaters, HVAC, battery storage, and electric vehicles—can provide ancillary grid services to mitigate reliability challenges caused by high penetration of renewable energy resources. It covers both academic aggregation methods and communication standards like IEEE 2030.5, OpenADR, and CTA-2045.

## 🔑 Key Arguments & Findings
* **Finding 1:** Weather-dependent, non-dispatchable RERs create scheduling challenges, reduce system inertia, and cause voltage variations, which can be addressed by aggregating residential-scale DER assets en masse to provide active grid services.
* **Finding 2:** Standardized open communication protocols (such as ANSI/CTA-2045, SunSpec Modbus, SAE J3072, IEEE 2030.5, and OpenADR) are essential to bridge customer-owned equipment and utility-scale DERMS, preventing proprietary vendor lock-in and ensuring grid interoperability.

## 🛠️ Methodological Notes / Technical Specifications
* **Standards Reviewed:** ANSI/CTA-2045 (physical modular interface), SunSpec Modbus (smart inverters), SAE J3072 (plug-in electric vehicles), IEEE 2030.5-2018 (SEP 2.0 application protocol), OpenADR 2.0 (demand response).
* **Ancillary Services Analyzed:** Frequency response, frequency regulation, ramp rate control, voltage/VAr compensation.
* **Testing Boundaries:** References testing at the National Renewable Energy Laboratory (NREL) and EPRI reports on CTA-2045.

## 💡 Personal Insights & Open Questions
* **Potential Application:** The overview of communication standards (specifically IEEE 2030.5) directly informs the architectural design of the EGoT microservices. EGoT services like DCAP, DERP, and MUP map directly to the SEP 2.0 application model analyzed in this review.
* **Gap/Next Step:** While the review outlines the open standards, it notes a lack of large-scale, field-proven implementations showing real-time, multi-objective aggregation of heterogeneous DERs (combining water heaters, smart inverters, and EVs) under a unified controller.

## 📌 Critical Quotes
> "By aggregating distributed energy resources en masse to provide grid services, grid operators can concurrently improve reliability while ensuring high penetration levels of renewable resources."
> "Academic researchers have developed the theoretical methods for achieving these objectives. Standards bodies have created open communication frameworks for linking these resources with grid operators."
