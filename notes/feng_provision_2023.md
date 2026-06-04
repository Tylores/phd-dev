# Provision of Contingency Frequency Services for Virtual Power Plants With Aggregated Models | Project Pillar: Methodology
**Date:** June 2026
**Status:** Peer-Reviewed Literature

## 🎯 Executive Summary
This paper proposes an equivalent aggregation model for Virtual Power Plants (VPPs) participating in contingency frequency reserve services. The model aggregates the dynamic response of thousands of heterogeneous DERs with diverse response latencies. Additionally, it constructs a performance-to-cost map and derives an analytical method to evaluate the marginal cost of DER latency deviations.

## 🔑 Key Arguments & Findings
*   **Finding 1:** heterogeneous response latencies and time constants among aggregated DERs significantly impact frequency stability. Aggregating DERs using a simple sum/average model without modeling latency fails to represent transient frequency dynamics, risking frequency collapse.
*   **Finding 2:** Using the Karush-Kuhn-Tucker (KKT) optimality conditions, the marginal cost of DER latency can be computed analytically in matrix form. This allows VPP operators to quantify the economic loss of latency and economically penalize DERs that deviate from reported latencies.

## 🛠️ Methodological Notes / Technical Specifications
*   **Modeling Framework:** Dynamic frequency response models, first-order transfer functions.
*   **Optimization:** Bi-level optimization, (e.g., converted to Mixed-Integer Quadratic Programming - MIQP), Gurobi solver.
*   **Test Systems:** IEEE 9-bus and modified CIGRE C6 test feeders.

## 💡 Personal Insights & Open Questions
*   **Potential Application:** Directly validates EGoT's reserve service lifecycle mapping and settlement verification (Scenario 2.3). It highlights the need to track and verify response latency and ramp rates during contingency events to enforce performance contracts.
*   **Gap/Next Step:** The proposed analytical penalty model assumes a centralized VPP aggregator with perfect knowledge of each DER's cost and physical parameters, which may violate ESI privacy principles of asset isolation.

## 📌 Critical Quotes
> "Due to the limited scale of individual DER units, they are collectively formed as a virtual power plant (VPP) to provide considerable frequency support capabilities during contingencies." (Page 2798)

> "The VPP should economically penalize DERs whose actual latency is larger than the reported latency so that DERs are encouraged to report the response latency accurately." (Page 2799)
---
