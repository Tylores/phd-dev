---
# Optimal Day-ahead Charging Scheduling of Electric Vehicles through an Aggregative Game Model | Project Pillar: Methodology
**Date:** May 2026
**Status:** Peer-Reviewed Literature

## 🎯 Executive Summary
This paper presents an aggregative game model for decentralized, day-ahead electric vehicle (EV) charging scheduling in electricity markets. Proving the existence and uniqueness of the pure strategy Nash equilibrium, the authors develop a quadratic programming method that allows individual EV controllers to minimize charging costs by considering their own driving patterns and their collective impact on spot prices.

## 🔑 Key Arguments & Findings
* **Finding 1:** As the market penetration of EVs grows, their collective charging demand begins to affect electricity spot prices. Standard charging scheduling that ignores this price feedback will lead to localized demand spikes, higher spot prices, and inflated charging costs.
* **Finding 2:** The proposed aggregative game model achieves the same optimal pricing outcome as a fully coordinated system, but without requiring communication or coordination among EV owners. Individual EV controllers automatically distribute their demand to prevent peak price spikes, benefiting both the grid and the EV owners.

## 🛠️ Methodological Notes / Technical Specifications
* Aggregative game theoretic model proving pure strategy Nash equilibrium.
* Solved using Quadratic Programming (QP) algorithms.
* Modeled using real-world driving data from the Danish National Travel Surveys and market prices from Nord Pool.
* Constraints: battery capacity limits, daily charging demand balance, charging availability, and maximum charging power.

## 💡 Personal Insights & Open Questions
* **Potential Application:** The decentralized aggregative game concept can be adapted in EGoT's Flow Reservation service (:8027) for electric vehicle fleets. This would allow EVs to schedule charging slots dynamically without overloading local transformers or driving up local prices.
* **Gap/Next Step:** The game model relies on a linear relationship between electricity price and aggregate demand ($\lambda_t = \alpha_t + \beta_t \cdot X_t$). How does the model perform under highly non-linear, multi-tier, or block tariff structures commonly used in distribution networks?

## 📌 Critical Quotes
> "When EV charging demand is considerable in a grid, it will impact spot prices in the electricity market and consequently influence the charging scheduling itself."
> "Without any coordination or communication between the EV controllers, the EV controllers distribute their own charging demand with proper amount over a few hours so that the demand will not congregate at a short period."
---
