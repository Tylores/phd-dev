# Photovoltaic Impact Assessment of Smart Inverter Volt-VAR Control on Distribution System Conservation Voltage Reduction and Power Quality | Project Pillar: Case Study
**Date:** May 2026
**Status:** Technical Documentation

## 🎯 Executive Summary
This NREL and SolarCity technical report assesses the impacts of distributed PV with autonomous smart inverter Volt-VAR control on Conservation Voltage Reduction (CVR) and power quality. The report proposes a novel single-index "Power Quality Score" (PQS) and evaluates it along with CVR energy savings using annual OpenDSS simulations of Hawaii (HECO) and California (PG&E) distribution systems.

## 🔑 Key Arguments & Findings
* **Finding 1:** Autonomous Volt-VAR control by distributed smart inverters mitigates local overvoltage and undervoltage issues, providing the flatter voltage profile required to expand conservation voltage reduction margins.
* **Finding 2:** Power quality cannot easily be represented by single parameters (like THD or voltage deviation) in isolation, so a composite Power Quality Score (PQS) is necessary to evaluate the net impact of voltage optimization and high PV penetration on grid performance.

## 🛠️ Methodological Notes / Technical Specifications
* **Simulation Engine:** OpenDSS (feeder models converted from CYME and Synergi via NREL's CYME2DSS and Synergi2DSS conversion tools).
* **Test Feeder Models:** Hawaii Electric Company (HECO) and Pacific Gas and Electric (PG&E) utility feeders.
* **Analysis Method:** Year-long, multi-scenario simulations varying PV penetration levels and smart inverter installation densities.
* **Evaluation Metrics:** CVR energy savings and the composite Power Quality Score (PQS).

## 💡 Personal Insights & Open Questions
* **Potential Application:** The concept of a composite Power Quality Score can be integrated into EGoT's data-export and OpenDSS simulation framework (`scripts/grid_services_sim.py`) to quickly evaluate the impact of different DER management strategies.
* **Gap/Next Step:** The detailed mathematical definition of the PQS weightings and how the parameters map to standard IEEE 1547 requirements is not fully elaborated in the extracted text.

## 📌 Critical Quotes
> "As a result, this report proposes a power quality scoring mechanism to measure the relative power quality of distribution systems using a single number, which is aptly named the 'power quality score' (PQS)."
> "Traditional CVR relies on operating utility voltage regulators and switched capacitors. However, with the increased penetration of distributed PV systems, smart inverters provide the new opportunity to control local voltage and power factor..."
---
