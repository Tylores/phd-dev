# Application of Advanced Metering Infrastructure Data to Advanced Utility System Operations | Project Pillar: Case Study
**Date:** May 2026
**Status:** Technical Documentation

## 🎯 Executive Summary
This CRADA final report documents a collaborative study between NREL and San Diego Gas & Electric (SDG&E) investigating the use of Advanced Metering Infrastructure (AMI) data to improve utility system operations. Using OpenDSS models of actual 12-kV feeders, the project evaluates PV smart inverter settings, develops tools for phase identification and meter-to-transformer mapping, and explores model-less control at the secondary distribution level.

## 🔑 Key Arguments & Findings
* **Finding 1:** Relying solely on net AMI billing measurements obscures behind-the-meter PV generation; separating load and PV profiles via disaggregation algorithms (using local solar irradiance data) is essential for accurate PV impact modeling.
* **Finding 2:** Evaluating standard inverter control curves (CA Rule 21, Hawaii Rule 14, IEEE 1547) reveals that custom co-simulations (such as integrating Python with OpenDSS to implement Volt-VAR-Watt controls) are necessary to effectively regulate voltages on feeders with high PV penetration.

## 🛠️ Methodological Notes / Technical Specifications
* **Simulations:** SDG&E feeder models translated from Synergi format into OpenDSS, paired with Python-based controllers for advanced inverter operations.
* **Tested Feeders:** 
  1. Feeder A: 12 kV, 10.3 MW peak, >5,000 customers, 341 service transformers, and ~70% PV capacity.
  2. Feeder B: 12 kV, 13.29 MW peak, 657 service transformers, and ~24% PV capacity.
* **Analyzed Curves:** California Rule 21, Hawaii Rule 14, IEEE 1547, and custom Volt-VAR-Watt controls.
* **Utility Tools Developed:** Phase identification algorithms, utility planning model anomaly detection, and meter-to-transformer mapping.

## 💡 Personal Insights & Open Questions
* **Potential Application:** The Python-OpenDSS integration methodology directly supports the validation of EGoT's grid services simulation scripts (`grid_services_sim.py`). It highlights the importance of incorporating PV disaggregation within EGoT's data export tool.
* **Gap/Next Step:** The report mentions "model-less control" in its objectives, but the details on the performance and stability limits of model-less controllers operating over latent, low-bandwidth AMI communication networks are not fully analyzed.

## 📌 Critical Quotes
> "High PV penetration levels in distribution feeders can cause operational challenges including voltage issues, reverse power flow, and protection issues."
> "The primary objective of the proposed project is to evaluate the capabilities of Advanced Metering Infrastructure (AMI) based controls for grid operations. This includes monitoring and control at the secondary transformer level..."
