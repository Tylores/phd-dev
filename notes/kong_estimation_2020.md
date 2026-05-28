---
# An estimation method of smart meter errors based on DREM and DRLS | Project Pillar: Methodology
**Date:** May 2026
**Status:** Peer-Reviewed Literature

## 🎯 Executive Summary
This paper proposes a remote estimation method for user smart meter errors and distribution line network losses. The approach uses a Dimension Reduction Estimation Model (DREM) via k-means clustering to handle model insolvability and a Damped Recursive Least Squares (DRLS) algorithm to ensure estimation stability and noise robustness.

## 🔑 Key Arguments & Findings
* **Finding 1:** Traditional on-site smart meter calibration is expensive and labor-intensive. Remote estimation using AMI big data is a viable alternative, but it is heavily affected by dynamic and unknown network losses in low-voltage distribution networks.
* **Finding 2:** By applying k-means clustering to group similar load measurements, the proposed DREM reduces the dimensionality of unknown network parameters. Combining this with DRLS (adding a damping factor to RLS) mitigates the risk of parameter explosion and enhances error convergence.

## 🛠️ Methodological Notes / Technical Specifications
* Two DREM variations: Current-Resistance (CR) model (highest accuracy, requires current measurements from the feeder meter) and Power-Loss (PL) model (slightly lower accuracy, but directly applicable with standard active power telemetry).
* DRLS algorithm with forgetting factor ($\lambda$) and damping factor ($\mu_0 = 0.01$).
* Test case: Validated in both laboratory and actual distribution feeder units ($s = 20$ clusters recommended).

## 💡 Personal Insights & Open Questions
* **Potential Application:** The DRLS and DREM methods could be applied to EGoT's Mirror Usage Point (MUP) data analysis to detect faulty virtual meters, calibration drift, or power theft/non-technical losses dynamically.
* **Gap/Next Step:** The model relies on linearizing non-linear relationships. How do highly non-linear load profiles, such as rapid EV charging pulses and intermittent PV generation, affect the accuracy of the k-means clustering membership matrix and subsequent error estimates?

## 📌 Critical Quotes
> "In this paper, a remote estimation method of smart meter errors based on Dimension Reduction Estimation Model (DREM) and Damped Recursion Least Squares (DRLS) is proposed..."
> "By applying the proposed method, the variation of smart meters state can be monitored timely, and online detection of power theft and leakage can be realized."
---
