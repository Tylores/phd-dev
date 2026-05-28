---
# The Credibility Modelling and Analysis of AMI Measurements for Distribution System State Estimation | Project Pillar: Methodology
**Date:** May 2026
**Status:** Peer-Reviewed Literature

## 🎯 Executive Summary
This paper addresses the challenge of non-synchronized data in Distribution System State Estimation (DSSE) due to communication delays in Advanced Metering Infrastructure (AMI). It proposes a statistical credibility model based on exponential distributions to dynamically adjust measurement weights in Weighted Least Squares (WLS) state estimation, yielding 95% confidence intervals for grid state variables.

## 🔑 Key Arguments & Findings
* **Finding 1:** In low-voltage and medium-voltage distribution systems, AMI measurements (e.g., active power) are collected sequentially and have random transmission delays of up to 30 minutes, which causes estimation divergence if treated as synchronized.
* **Finding 2:** Historical high-sampling-rate smart meter data reveals that relative load variation between near real-time (delayed) and real-time measurements follows an exponential distribution. Utilizing this to update the measurement covariance matrix $R$ reduces estimation errors significantly, closer to actual synchronized states.

## 🛠️ Methodological Notes / Technical Specifications
* Weighted Least Squares (WLS) state estimation using Newton-Raphson iterations.
* Credibility model based on relative load variation ($\lambda_p$), shown to follow an exponential distribution at a 95% confidence level.
* Time segmentation: 4 daily segments (valley, peaks, flat).
* Validated on a 116-node low-voltage distribution network with mixed SCADA (1 min updates) and AMI (15 min updates with up to 30 min random delays).

## 💡 Personal Insights & Open Questions
* **Potential Application:** Direct value for EGoT's telemetry services (MUP) and state estimation logic. Rather than assuming all IEEE 2030.5 smart meter readings are perfectly synchronized, we can weight them dynamically based on their age (delay) to prevent state estimation divergence in distribution network models.
* **Gap/Next Step:** Can this credibility model be extended to reactive power and volt-var control, where delays in voltage measurements might cause hunting or instability in smart inverter controllers?

## 📌 Critical Quotes
> "However, smart meter measurements often are not synchronized which may cause inaccuracy and divergence when directly applied to distribution system state estimation (DSSE)."
> "To applicate the credibility model, the measurement weight is assumed to consist of two components... equipment error and measurement arrival delay."
---
