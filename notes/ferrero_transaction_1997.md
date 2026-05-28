# Transaction Analysis in Deregulated Power Systems Using Game Theory | Project Pillar: Literature Review
**Date:** May 2026
**Status:** Peer-Reviewed Literature

## 🎯 Executive Summary
This paper proposes a game-theoretic methodology to simulate and analyze the strategic pricing and bidding behavior of participants in deregulated electricity markets. Utilizing cooperative and non-cooperative game theory on a modified IEEE 30-bus system, the authors show how market design and network transmission constraints influence coalition formation and market power.

## 🔑 Key Arguments & Findings
* **Finding 1:** Deregulated market participants prioritize individual profit maximization over system-wide efficiency, necessitating pool rules that incentivize cooperative behavior (the "grand coalition") and discourage anticompetitive coalitions.
* **Finding 2:** Network transmission constraints create physical bottlenecks that participants can exploit through strategic pricing, showing that physical grid topology directly shapes economic game equilibria.

## 🛠️ Methodological Notes / Technical Specifications
* **Theoretical Framework:** Cooperative and non-cooperative game theory, utilizing max-min (minimax) strategy selection and iterative dominance.
* **Network Model:** Modified IEEE 30-bus system.
* **Mathematical Modeling:** Quadratic generation cost curves, linear price bidding curves, and Spot Pricing formulations using Lagrange multipliers for transmission line flow constraints.
* **Computational Aspect:** Evaluates $2^N - 1$ potential coalitions (where $N$ is the number of players/utilities).

## 💡 Personal Insights & Open Questions
* **Potential Application:** The transactional modeling of competitive agents is relevant to EGoT's FlowReservation system. If multiple aggregator clients compete for limited distribution transformer capacity, game-theoretic modeling can help analyze if they will bid honestly or try to game the reservation system.
* **Gap/Next Step:** The paper notes that simulating a realistic number of market players (e.g., dozens of generators) is computationally prohibitive. Scaling this to thousands of DER nodes in distribution networks requires hierarchical abstractions that are not explored in this work.

## 📌 Critical Quotes
> "In a deregulated energy marketplace, participants are interested in maximizing their own profits, regardless of the system-wide profits."
> "Pool regulations should prevent any coalitions other than the grand coalition, and encourage cooperation among Pool members."
---
