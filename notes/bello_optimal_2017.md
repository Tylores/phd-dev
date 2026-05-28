# Optimal Settings for Multiple Groups of Smart Inverters on Secondary Systems Using Autonomous Control | Project Pillar: Methodology
**Date:** May 2026
**Status:** Peer-Reviewed Literature

## 🎯 Executive Summary
This paper presents a methodology for determining optimal autonomous control settings (e.g., Volt-VAR and Volt-Watt) for smart inverters installed on secondary distribution systems. Using OpenDSS to perform detailed annual time-series simulations on a high-fidelity utility feeder model, the authors analyze how different inverter settings impact system losses, voltage violations, and voltage variability at customer service drops.

## 🔑 Key Arguments & Findings
* **Finding 1:** Optimal smart inverter settings are highly dependent on the chosen operational objective (e.g., minimizing line losses vs. mitigating voltage violations) and current grid conditions, necessitating dynamic or multi-objective curve optimization.
* **Finding 2:** Although primary voltage regulating devices (like substation transformers and capacitors) may remain insensitive at low PV/smart-inverter penetrations (under 5% capacity), customer-side secondary voltage profiles show significant sensitivity, making secondary grid modeling critical.

## 🛠️ Methodological Notes / Technical Specifications
* **Simulation Software:** Open-source Distribution System Simulator (OpenDSS).
* **Model Resolution:** Detailed representation of medium-voltage lines, distribution transformers, secondary service drops, and individual customer loading profiles.
* **Feeder Characteristics (Feeder XYZ):** 12.47 kV nominal, 9,900 kW peak load, 0.9 power factor, 7,200 kvar capacitors.
* **Evaluated Functions:** Fixed Power Factor control, autonomous Volt-VAR (with and without deadbands, and inductive-only modes), and Volt-Watt control.

## 💡 Personal Insights & Open Questions
* **Potential Application:** Strongly supports EGoT's detailed microservices modeling. In particular, it underscores the need for EGoT's DER and DERP services to model secondary services and transformers rather than just aggregating customer loads at the primary level when designing Volt-VAR controls.
* **Gap/Next Step:** The study evaluates static, pre-configured Volt-VAR curve options. Investigating how the EGoT platform can dynamically distribute optimal Volt-VAR settings (e.g., via the DERP service) based on real-time feeder loading or solar forecasts remains a key next step.

## 📌 Critical Quotes
> "For Feeder XYZ, in order to reduce the losses, the smart inverters on the secondary system has to be aggressive and inductive with no deadband."
> "The best inverter settings are dependent on performance metrics (losses, voltage variability index, feeder voltage flattening, time below ANSI etc.), feeder characteristics, load and solar condition..."
