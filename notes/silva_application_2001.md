# Application of mechanism design to electric power markets | Project Pillar: Methodology
**Date:** May 2026
**Status:** Peer-Reviewed Literature

## 🎯 Executive Summary
This paper applies the economic theory of mechanism design to solve the asymmetric information problem in deregulated electric power markets. It introduces a bidding mechanism that ensures Pareto-efficient economic dispatch by incentivizing competing generators to truthfully report their private marginal costs, even under transmission congestion.

## 🔑 Key Arguments & Findings
* **Finding 1:** Direct economic dispatch fails in a competitive environment because generators have a strategic incentive to exaggerate their marginal costs to secure higher cleared prices or guaranteed generation allocations.
* **Finding 2:** Under mechanism design principles, payment and production allocations can be mathematically structured such that truthful cost reporting constitutes a Bayesian-Nash equilibrium (generators maximize profits by bidding truthfully).

## 🛠️ Methodological Notes / Technical Specifications
* **Grid Modeling:** Uses the DC power flow model.
* **Physical Assumptions:** Assumes static load demands, linear generator cost functions (constant marginal costs), and a bounded, continuous probability distribution of marginal costs.
* **Validation Case:** Demonstrated using simulations on the standard IEEE 14-bus test system.

## 💡 Personal Insights & Open Questions
* **Potential Application:** Designing peer-to-peer or local transactive energy markets for EGoT. Applying mechanism design to local DER programs can help mitigate strategic gaming by residential battery or PV owners during demand response/congestion events.
* **Gap/Next Step:** The model relies on simplified linear costs and static loads, whereas real-world distribution systems involve highly dynamic, non-linear loads and battery state-of-charge constraints that are hard to capture in static Bayesian-Nash formulations.

## 📌 Critical Quotes
> "When generator companies compete with one another in a deregulated market, they may not be willing to share the information needed to perform an economic dispatch of the generation."
---
