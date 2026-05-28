# Guidance on the usability-privacy tradeoff for utility customer data aggregation | Project Pillar: Literature Review
**Date:** May 2026
**Status:** Peer-Reviewed Literature

## 🎯 Executive Summary
This paper analyzes the usability-privacy tradeoff of utility customer data (UCD) release in Los Angeles, presenting statistical guidelines for aggregate data publication. It shows that disclosure risks vary by utility type (electricity, gas, water) and economic sector, and provides recommendations for ethically balanced, aggregated data release that benefits urban planners while preserving tenant anonymity.

## 🔑 Key Arguments & Findings
* **Finding 1:** Rulemaking on utility customer data (UCD) privacy is often overly restrictive, blocking access to big data that is critical for municipal carbon emissions, water conservation planning, and empirical evaluation of energy efficiency investments.
* **Finding 2:** A systematic tradeoff exists where spatial or temporal aggregation preserves privacy (reducing disclosure risk) but reduces data usability; this tradeoff varies significantly between residential sectors (which can be aggregated safely using spatial bins) and commercial/industrial sectors (where large single customers dominate and can easily be re-identified).

## 🛠️ Methodological Notes / Technical Specifications
* **Case Study / Data:** Account-level consumption of water, electricity, and natural gas in Los Angeles.
* **Aggregation Standard Analyzed:** "15/15 rule" (e.g. at least 15 customers per bin, and no single customer representing >15% of the consumption) compared to HIPAA and other standards.
* **Statistical Methods:** Data de-identification, k-anonymity (e.g. KIPDA), microaggregation.

## 💡 Personal Insights & Open Questions
* **Potential Application:** When EGoT exports telemetric data for municipal grid reviews or research purposes (e.g., using the data-export tool to output CSVs for OpenDSS or other analysis), we can implement a "15/15 rule" filter or similar k-anonymity checks to ensure that individual prosumers are not re-identified.
* **Gap/Next Step:** The paper focuses on static database aggregation for public research. How does this usability-privacy trade-off adapt to real-time, streaming telemetry required for active grid operations (e.g., direct control loop feedback in DERMS) where data must be transmitted instantly without batch aggregation delays?

## 📌 Critical Quotes
> "Modern cities, along with their researchers and innovators can benefit from applying 'big data' to their sustainability and infrastructure problems and policies, e.g., water and energy consumption."
> "...current utility customer data (UCD) privacy rulemaking fails to ensure safe release of these data for the public benefit and does not currently strike a sound balance between the competing values of usability and privacy."
