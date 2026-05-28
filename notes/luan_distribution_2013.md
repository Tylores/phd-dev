---
# Distribution network topology error correction using smart meter data analytics | Project Pillar: Methodology
**Date:** May 2026
**Status:** Peer-Reviewed Literature

## 🎯 Executive Summary
This paper introduces an algorithm developed by BC Hydro that utilizes customer smart meter hourly voltage profiles to detect and correct topology errors (such as wrong transformer connections or feeder phase assignments) in utility GIS records. The algorithm calculates the voltage at the point of coupling ($V_{pc}$) to eliminate service wire length differences, analyzing correlation factors and relative magnitude rankings to reconstruct the correct distribution tree.

## 🔑 Key Arguments & Findings
* **Finding 1:** Errors in GIS topology records (like customers linked to the wrong transformer or phase) are common and degrade the performance of Volt-Var optimization (VVO), outage response, and asset load planning. Manual correction is too time-consuming and expensive.
* **Finding 2:** Customer voltage profiles share strong temporal correlation if they are connected to the same transformer/feeder branch, and their magnitudes rank strictly based on upstream/downstream location due to line losses. Comparing these profiles (specifically calculating $V_{pc} = V_{meter} + I_{meter} \cdot Z_{service}$) allows precise detection of misaligned meters and accurate repositioning.

## 🛠️ Methodological Notes / Technical Specifications
* Formula for coupling point voltage: $V_{pc} = V_{meter} + I_{meter} \cdot Z_{service}$, where current $I_{meter}$ can be estimated as $kWh/V_{meter}$ if not measured directly.
* Uses Pearson correlation coefficient matrices to group adjacent meters on secondary branches.
* Tested on actual BC Hydro distribution systems, successfully identifying misclassified transformers, phase imbalances (a phase A transformer actually on phase B), and overloaded assets.

## 💡 Personal Insights & Open Questions
* **Potential Application:** Directly applicable to EGoT's telemetry backend. Using the correlation of voltages from different Mirror Usage Points (MUPs) can validate the virtual grid topology model in our simulator without manual checks.
* **Gap/Next Step:** The calculation of $V_{pc}$ requires knowledge of the service wire impedance ($Z_{service}$). If the GIS records have incorrect or missing wire sizes/lengths, how sensitive is the algorithm to errors in $Z_{service}$ estimation?

## 📌 Critical Quotes
> "Starting with the distribution network topology information available in enterprise GIS, the proposed analytic approach uses smart meter data to detect wrongly connected customers in a transformer neighborhood..."
> "A wrong topology model will result in wrongly presented load flow in the network, which makes it impossible for system optimization such as Voltage and Var Optimization to achieve the desired performance level."
---
