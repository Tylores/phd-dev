# Balancing Accuracy and Complexity in Optimisation Models of Distributed Energy Systems and Microgrids with Optimal Power Flow: A Review | Project Pillar: Literature Review
**Date:** May 2026
**Status:** Peer-Reviewed Literature

## 🎯 Executive Summary
This paper presents a comprehensive review of the design and operational optimization models used for distributed energy systems (DES) and microgrids, addressing the gap between process system optimization and electrical grid physics. The authors emphasize that incorporating optimal power flow (OPF) constraints is essential to prevent physically infeasible dispatch schedules and recommend bridging the gap between simplified linear models and high-fidelity AC network simulations.

## 🔑 Key Arguments & Findings
* **Finding 1:** Traditional DES design and dispatch optimization models frequently neglect or oversimplify the nonlinear and nonconvex constraints of alternating current (AC) power flow, which risk producing mathematically optimal schedules that violate real-world grid voltage or thermal limits.
* **Finding 2:** Incorporating detailed AC-OPF constraints into microgrid models (forming a class of models termed DES-OPF) via advanced optimization tools (e.g., SOCP, MINLP, and ADMM) is crucial; achieving physically feasible solutions on high-fidelity models takes precedence over global optimality on inaccurate, linear approximations.

## 🛠️ Methodological Notes / Technical Specifications
* **Optimization Classes Reviewed:** Linear Programming (LP), Mixed-Integer Linear Programming (MILP), Mixed-Integer Nonlinear Programming (MINLP), Second Order Cone Programming (SOCP), and heuristic algorithms (GA, PSO).
* **Distributed & Real-Time Frameworks:** Alternating Direction Method of Multipliers (ADMM), Dynamic Programming (DP), and Model Predictive Control (MPC).
* **Grid Simulation Tools Highlighted:** OpenDSS, GridLAB-D, PowerFactory, OATS, and PyPSA.
* **Scope:** 14,301-word interdisciplinary review linking chemical process engineering, power systems engineering, and microgrid planning.

## 💡 Personal Insights & Open Questions
* **Potential Application:** Heavily validates EGoT's methodology of running OpenDSS simulations (`grid_services_sim.py`) alongside microservice emulators. It confirms that EGoT's services (like FlowReservation and DERP) must enforce AC constraints rather than simple volumetric power limits.
* **Gap/Next Step:** While the review identifies the need for high-fidelity DES-OPF models, it notes a lack of standardized benchmarking datasets that allow researchers to evaluate the trade-offs between optimization speed, algorithm complexity, and physical feasibility in real-time edge environments.

## 📌 Critical Quotes
> "Optimisation and simulation models for the design and operation of grid-connected distributed energy systems (DES) often exclude the inherent nonlinearities related to power flow and generation... Such models may provide sub-optimal or even infeasible designs and dispatch schedules."
> "Results of these studies suggest that achieving feasible solutions with high-fidelity models is more important than achieving globally optimal solutions using less-detailed DES models."
