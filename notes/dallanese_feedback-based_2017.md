# Feedback-based projected-gradient method for real-time optimization of aggregations of energy resources | Project Pillar: Methodology
**Date:** May 2026
**Status:** Peer-Reviewed Literature

## 🎯 Executive Summary
This paper develops a real-time, online optimization method based on a projected-gradient algorithm to coordinate aggregations of heterogeneous distributed energy resources (DERs) in multiphase distribution networks. By integrating physical grid measurements (feedback) directly into the algorithm's iteration step, the method bypasses the need for pervasive metering, accommodates AC power flow model inaccuracies, and scales to subsecond optimization timescales.

## 🔑 Key Arguments & Findings
* **Finding 1:** Batch optimization is computationally impractical for subsecond control of heterogeneous DERs and is highly sensitive to distribution network model errors; incorporating physical measurements directly into the gradient step resolves both limitations.
* **Finding 2:** To handle nonconvex or discrete DER operational sets (e.g., EVs or water heaters), their feasible regions can be convexified during setpoint optimization, with the resulting continuous setpoints mapped back to discrete states using an error-diffusion algorithm.

## 🛠️ Methodological Notes / Technical Specifications
* **Mathematical Core:** Online projected-gradient descent method modified to incorporate physical measurements of aggregate power flow ($\hat{p}_0$) and individual device outputs ($\hat{x}_{j,\varphi}$).
* **Update Interval:** Designed for subsecond or second-level time steps ($\delta$).
* **Network Representation:** Linear sensitivity matrix ($M$) representing voltage and power flow dependencies on a multiphase AC distribution network.
* **Discrete/Nonconvex Handling:** Feasible sets are replaced by their convex hulls, and a variant of the error-diffusion algorithm (delta-sigma modulation style) maps the continuous outputs to discrete device states.

## 💡 Personal Insights & Open Questions
* **Potential Application:** Directly applicable to EGoT's DER control loop. Emulators (`emulator-der`) can execute these lightweight feedback-based updates using voltage and power measurements from the Mirror Usage Point (MUP) service, avoiding full OPF calculations on substation servers.
* **Gap/Next Step:** The study assumes immediate feedback and negligible communication delays. Investigating how communication latency, network congestion, or temporary packet losses between the aggregator and the DERs impact the stability and convergence of the projected-gradient loop is a vital next step.

## 📌 Critical Quotes
> "By virtue of this approach, the resultant algorithm can cope with inaccuracies in the representation of the AC power ﬂows, it avoids pervasive metering to gather the state of noncontrollable resources, and it naturally lends itself to a distributed implementation."
> "The design of the online algorithm is based on a projected-gradient method, suitably modiﬁed to accommodate appropriate measurements from the distribution network and the DERs."
