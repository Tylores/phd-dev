# Privacy-Functionality Trade-Off: A Privacy-Preserving Multi-Channel Smart Metering System | Project Pillar: Methodology
**Date:** June 2026
**Status:** Peer-Reviewed Literature

## 🎯 Executive Summary
This paper proposes a multi-channel smart metering architecture that addresses the trade-off between user privacy and utility functionality. By utilizing substation-level data aggregation and data down-sampling alongside a local Home Area Network (HAN) private platform, the system performs local billing calculations and publishes zero-knowledge commitments, preventing fine-grained usage profiles from leaving the premises.

## 🔑 Key Arguments & Findings
*   **Finding 1:** Aggregating smart meter data at the distribution substation level (minimum size of 50 houses) effectively blinds NILM adversaries, reducing appliance disaggregation F-scores to zero, while still providing high-frequency (100 Hz) telemetry for grid operators.
*   **Finding 2:** Performing TOU billing calculations locally on a HAN private platform and transmitting monthly totals with Pedersen zero-knowledge commitments allows utilities to verify billing correctness without ever accessing individual high-frequency load profiles.

## 🛠️ Methodological Notes / Technical Specifications
*   **System Components:** Substation-level smart meters, HAN private platforms, utility verifiers.
*   **Privacy Techniques:** Zero-Knowledge Proof (ZKP) billing verification, data down-sampling (from 1-min to monthly), differential privacy (DP-SGD) deep learning NILM.
*   **Dataset:** Dataport (US) containing 1-minute resolution electricity data from 722 houses during 2018.

## 💡 Personal Insights & Open Questions
*   **Potential Application:** Directly supports EGoT's privacy preservation tenets and database segregation. The local billing and zero-knowledge proof verification logic provides a theoretical pathway to secure EGoT's billing endpoints (`/bill` and `/mup`) without collecting raw telemetry.
*   **Gap/Next Step:** The implementation requires significant computation power on local smart home processors to compute zero-knowledge commitments. The feasibility and cost of deploying these edge processors for mass roll-out are left unaddressed.

## 📌 Critical Quotes
> "In the proposed system, the smart meter plays the role of assistant processor rather than information sender/receiver, and it enables three communication channels to protect privacy and allow freedom of choice." (Page 1)

> "From the evaluation, the conclusion is made a dataset with aggregation size over 50, and interval resolution larger than 24 h can overcome both data sensitivity and algorithm sensitivity." (Page 22)
---
