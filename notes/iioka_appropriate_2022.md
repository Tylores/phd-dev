---
# Appropriate Volt–Var Curve Settings for PV Inverters Based on Distribution Network Characteristics Using Match Rate of Operating Point | Project Pillar: Methodology
**Date:** May 2026
**Status:** Peer-Reviewed Literature

## 🎯 Executive Summary
This paper proposes a method to optimize Volt-Var curve parameters for PV inverters using a new evaluation index called "match rate," which measures how well the inverter's operating points conform to the Volt-Var curve under power factor constraints. Testing across five distribution models shows that the optimized settings significantly reduce line losses and voltage violations while minimizing unnecessary reactive power output.

## 🔑 Key Arguments & Findings
* **Finding 1:** Under active power priority and power-factor constraints, smart inverters often fail to follow the commanded Volt-Var curve because their reactive power capacity is limited. The proposed "match rate" index successfully quantifies this deviation to help select curves that are physically achievable.
* **Finding 2:** Selecting the Volt-Var curve that minimizes reactive power output while avoiding voltage violations reduces distribution line losses and avoids unnecessary coordination conflicts with legacy on-load tap changers (LTC/LRT).

## 🛠️ Methodological Notes / Technical Specifications
* Five actual Japanese distribution line models (residential, rural, and industrial areas) with Load Ratio control Transformers (LRT/LTC).
* 360 candidate patterns of Volt-Var curves defined by central voltage ($V_{ref}$), dead zone, and slope.
* Evaluation metrics: line losses, voltage violations, number of LRT tap operations, and match rate.

## 💡 Personal Insights & Open Questions
* **Potential Application:** Use the "match rate" concept to evaluate DER control settings in EGoT's DERP (DER Program) and simulation platform (e.g., in OpenDSS runs), ensuring that simulated smart inverters operate within their actual capability limits.
* **Gap/Next Step:** How does the match rate degrade under rapid solar irradiance fluctuations when real-time active power changes dynamically, and how should dynamic Volt-Var curves adapt?

## 📌 Critical Quotes
> "When a power-factor constraint is imposed on the PV inverter, it may not output the reactive power according to the volt–var curve depending on the active power output. The match rate is an index to show the percentage of the operating points of the PV inverter that conform with the volt–var curve."
> "The volt–var function of smart inverters is expected to improve the voltage controllability of the distribution system. However, the appropriate shape of the volt–var curve for the volt–var function is not clear."
---
