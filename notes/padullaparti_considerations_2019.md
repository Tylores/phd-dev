# Considerations for AMI-Based Operations for Distribution Feeders | Project Pillar: Technical Specs
**Date:** May 2026
**Status:** Peer-Reviewed Literature

## 🎯 Executive Summary
This paper examines considerations for operationalizing large AMI datasets for distribution feeder analysis, focusing on phase identification. It demonstrates that traditional regression-based phase identification fails under high PV generation due to voltage masking but shows that statistical clustering methods can accurately determine customer phase connectivity using just 1 day of 5-minute averaged AMI data.

## 🔑 Key Arguments & Findings
* **Finding 1:** Accurate phase connectivity models are crucial for advanced distribution automation and volt-var controls, but existing phase database records are highly inaccurate due to reconfigurations and restoration activities.
* **Finding 2:** Traditional linear regression phase estimation methods break down when PV penetration exceeds 20% due to solar intermittency masking voltage profiles; advanced statistical methods are necessary to isolate the PV signature and identify phases.

## 🛠️ Methodological Notes / Technical Specifications
* **Sample Size / Model:** Actual distribution feeder model from San Diego Gas & Electric (SDG&E) serving 548 customers (peak demand: 10.3 MW, 30% PV penetration, 4,213 total nodes).
* **Data Resolution:** Evaluates data granularities from 1-minute to 30-minute intervals. 5-minute averaged active/reactive power and per-phase voltage are typical.
* **Tools Used:** GridPV tool, QSTS (quasi-static time-series) simulations.
* **Findings on Data Requirements:** 1 day of AMI data is sufficient to identify phase connectivity accurately. The algorithms are generally robust to data resolution reductions down to 30 minutes.

## 💡 Personal Insights & Open Questions
* **Potential Application:** In the EGoT emulation platform, smart meter telemetry (e.g., exported to CSV for OpenDSS simulation) can be analyzed using these statistical phase identification algorithms to verify that modeled phase connectivity matches simulated network profiles, detecting mapping errors automatically.
* **Gap/Next Step:** The methods are validated using synthetic AMI data generated via clean QSTS simulation. Real-world smart meter data contains measurement noise, communication dropouts, and time-synchronization errors. How do these algorithms perform under high data-loss scenarios?

## 📌 Critical Quotes
> "The results of this study show that the phase connectivity, even in the presence of high PV generation, can be accurately identified using statistical analysis of AMI data of 1 day."
> "Existing phase identification techniques... fail to identify the phases accurately when considerable PV generation is present as the features used in these methods ignore the impact of PV generation in forming the voltage prediction models."
