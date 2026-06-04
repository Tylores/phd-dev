# Towards Optimality Preserving Aggregation for Scheduling Distributed Energy Resources | Project Pillar: Methodology
**Date:** June 2026
**Status:** Peer-Reviewed Literature

## 🎯 Executive Summary
This paper investigates the mathematical aggregation of heterogeneous energy-constrained DERs (EC-DERs), such as storage batteries and flexible loads. It shows that simple interval sum aggregation methods enlarge the feasible schedule space, leading to physically tracking-infeasible schedules. The authors derive sufficient conditions and a "consistent dispersion" rule that guarantees exact, recursively feasible aggregated scheduling without any loss of optimality.

## 🔑 Key Arguments & Findings
*   **Finding 1:** Aggregating DERs by simply summing individual power and energy boundaries ignores the reachability properties of the underlying devices, resulting in aggregated schedules that cannot be dispersed to individual devices without violating their physical constraints.
*   **Finding 2:** Enforcing a "consistent dispersion" optimization step at each time interval guarantees that the aggregated time-varying battery model matches the exact feasible set of the fully disaggregated model, ensuring recursive feasibility.

## 🛠️ Methodological Notes / Technical Specifications
*   **Mathematical Models:** Time-varying battery models, Minkowski sums and differences, optimal control formulations.
*   **Optimization:** Problem reduction, linear programming, quadratic programming.
*   **Validation Case Study:** Simulation of 100 domestic batteries with time-independent power limits and time-varying energy constraints.

## 💡 Personal Insights & Open Questions
*   **Potential Application:** Directly supports EGoT's Flow Reservation scheduling and reservation engine. It provides the mathematical proof that abstracting DER capacities as unified power-flow boundaries (Pillar 3 - Provider-Side Aggregation) can be mathematically exact and feasible.
*   **Gap/Next Step:** The proposed framework neglects conversion losses and reactive power flow, which are critical in physical distribution grids and must be modeled to extend the applicability of the aggregation.

## 📌 Critical Quotes
> "Reducing the number of decision variables by means of aggregation can help alleviate these issues. However, despite the frequent use of aggregation for populations of storage devices, few works in the literature provide formal justification." (Page 1477)

> "Whenever the energy states of the individual devices satisfy a specific (collective) property—existence of a consistent dispersion... the relaxed aggregation does not alter the feasible set and, thus, does not imply any optimality loss." (Page 1486)
---
