---
# Privacy Protection via Joint Real and Reactive Load Shaping in Smart Grids | Project Pillar: Methodology
**Date:** May 2026
**Status:** Peer-Reviewed Literature

## 🎯 Executive Summary
This paper addresses consumer privacy protection against nonintrusive appliance load monitoring (NIALM) in smart grids. It proposes a joint real and reactive load shaping multi-objective optimization framework that demonstrates a twofold increase in privacy preservation compared to traditional real-power-only load shaping.

## 🔑 Key Arguments & Findings
* **Finding 1:** Smart meters measure both real and reactive power, and NIALM techniques exploit reactive power signatures to infer private appliance usage. Thus, shaping only real power leaves significant privacy vulnerabilities via reactive power.
* **Finding 2:** Joint shaping of real and reactive power reduces mutual information (information leakage) by over 52% compared to shaping only one component, with only a modest increase in consumer cost (<8%) and discomfort (<20%).

## 🛠️ Methodological Notes / Technical Specifications
* Mixed-Integer Programming (MIP) model utilizing minimax goal programming for Pareto efficiency.
* System utilizes rechargeable batteries (RBs) for real power shaping and capacitors for reactive power shaping.
* Data sets used: ACS-F2 database for appliance consumption signatures and AMPds (Makonin et al. 2016) database.
* Privacy metrics: Mutual Information (MI) between actual appliance load and metered load.

## 💡 Personal Insights & Open Questions
* **Potential Application:** In EGoT’s Mirror Usage Point (MUP) and metering telemetry services, we should be aware of the privacy implications of high-resolution active/reactive power readings. Incorporating privacy-enhancing load shaping rules in home DER controllers (using inverter reactive power control rather than dedicated capacitors) presents a practical extension.
* **Gap/Next Step:** The authors note that PV smart inverters could be used for reactive power shaping to avoid needing physical household capacitors. Can we implement this joint active/reactive load shaping directly on the EGoT smart inverter emulation framework?

## 📌 Critical Quotes
> "Joint shaping of real and reactive power components results in the best possible privacy preservation performance, which leads to more than a twofold increase in privacy in terms of mutual information."
> "Future research directions include exploiting amenities such as batteries and PV generators for shaping real and reactive load simultaneously without the need for a household capacitor."
---
