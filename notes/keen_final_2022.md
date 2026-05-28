---
# Final Technical Report: Improving Solar and Solar+Storage Screening Techniques to Reduce Utility Interconnection Time and Costs | Project Pillar: Methodology
**Date:** May 2026
**Status:** Technical Documentation

## 🎯 Executive Summary
This NREL technical report evaluates data-driven secondary network modeling and hosting capacity screening techniques to speed up and reduce the cost of residential solar and solar+storage interconnection. Power flow models with predicted secondary topologies and data-driven methods improved the screen success rate by up to 55 percentage points compared to traditional utility screening shortcuts.

## 🔑 Key Arguments & Findings
* **Finding 1:** Traditional utility screening heuristics (such as the 15% of peak load screen) are often overly conservative or inaccurate. The proposed decision tree method predicts secondary network topologies and logistic regression predicts conductors using commonly available GIS and service transformer data, which robustly handles bad GIS data.
* **Finding 2:** Once the primary and secondary models are built, hosting capacity results can be used to train random forest models to predict application pass/fail rates. This represents a "right-sized" screening approach for low-risk, high-volume residential interconnection requests.

## 🛠️ Methodological Notes / Technical Specifications
* Decision tree classifier used for secondary topology prediction based on service transformer, customer, and street locations.
* Logistic regression for secondary conductor prediction (based on real-world object types, transformer ratings, conductor length, and distance).
* Random forest model for predicting pass/fail likelihood of PV interconnection applications.
* Testing evaluated on synthetic distribution models (e.g., SMART-DS) and real utility networks (like Pepco and Xcel).

## 💡 Personal Insights & Open Questions
* **Potential Application:** The insights on secondary network estimation (specifically predicting conductor impedance and topology from customer/transformer locations) can help refine default circuit models in EGoT’s OpenDSS simulations when secondary GIS data is incomplete.
* **Gap/Next Step:** The report mentions the challenge of varying inverter settings (legacy vs. smart inverters with different setpoints) on the same feeder. How can dynamic DER programs (like IEEE 2030.5 DERP) be factored into these screening/hosting capacity algorithms when the controls are time-varying and state-dependent?

## 📌 Critical Quotes
> "Powerflow based models with predicted secondaries and data-driven methods both increased the screening success rate, relative to common utility heuristics, by as much as 55 percentage points."
> "Data-driven screening techniques were described by one utility as a “right-sized” approach for residential customers given the low-risk of small errors and the high-cost of accurate modeling."
---
