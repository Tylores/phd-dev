---
# Optimal Parameters of Volt–Var Function in Smart Inverters for Improving System Performance | Project Pillar: Methodology
**Date:** May 2026
**Status:** Peer-Reviewed Literature

## 🎯 Executive Summary
This paper proposes a method to optimize the parameters of a smart inverter's Volt-Var curve using a multi-objective optimization framework. Quasi-static time-series simulations in OpenDSS on a South Korean feeder model verify that adjusting objective weights can minimize voltage deviations, line losses, and reactive power peaks to prevent curtailment of PV active power.

## 🔑 Key Arguments & Findings
* **Finding 1:** Standard, static Volt-Var curves (like default settings) often fail to balance multiple grid performance indicators. Utilizing a multi-objective function allows the utility to weight different priorities (e.g., voltage deviations, system losses, and reactive power peaks).
* **Finding 2:** Restricting the peak reactive power of the smart inverter prevents it from hitting active power curtailment limits (due to inverter capacity limits). By configuring weights, system losses can be reduced by 6.2% and reactive power peaks by 75% compared to standard, non-optimized curves.

## 🛠️ Methodological Notes / Technical Specifications
* Simulated on a representative South Korean distribution feeder model using OpenDSS for quasi-static time-series (QSTS) simulation with 1-year of load/PV profiles.
* Multi-objective optimization solved using Particle Swarm Optimization (PSO) to determine Volt-Var curve parameters ($V_1, V_2, V_3, V_4$ and $Q_1, Q_2$).
* Compares five weighting cases: Case A (standard settings), Case B (equal weights), Case C (voltage focus), Case D (loss focus), and Case E (reactive peak focus).

## 💡 Personal Insights & Open Questions
* **Potential Application:** The use of OpenDSS for evaluating Volt-Var settings directly relates to EGoT's OpenDSS simulation capabilities (`grid_services_sim.py`). We can implement the multi-objective Volt-Var curve selection logic in our grid service simulation script.
* **Gap/Next Step:** Can these optimal parameters be dynamically updated via IEEE 2030.5 DER control parameters (`DERControl` settings) in response to seasonal or weekly load changes, and what is the communication cost?

## 📌 Critical Quotes
> "This paper verified the proposed method through OpenDSS, a quasi-static time-series simulation, for the test model considering the characteristics of the distribution system in South Korea."
> "Through the test model... this paper verified that the over-voltage problem caused by the high penetration of the distributed generation was solved by the volt–var function."
---
