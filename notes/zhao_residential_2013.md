# Residential demand response with power adjustable and unadjustable appliances in smart grid | Project Pillar: Methodology
**Date:** May 2026
**Status:** Peer-Reviewed Literature

## 🎯 Executive Summary
This paper investigates residential demand response (DR) scheduling by classifying appliances into deferrable/undeferrable and adjustable/unadjustable. It focuses on continuously adjustable HVAC systems (which represent 72% of typical household load) to minimize electricity bills under real-time pricing while maintaining indoor comfort.

## 🔑 Key Arguments & Findings
* **Finding 1:** Focusing DR programs exclusively on deferrable appliances (like washing machines) yields low peak-reduction returns because they constitute less than 8% of average household consumption compared to thermal loads (72%).
* **Finding 2:** Formulating HVAC scheduling as a convex optimization problem under comfortable temperature bounds can reduce electricity costs by up to 25% (and PAR by 63%) with non-causal load forecasts, and by 10% (and PAR by 28%) using real-time causal control.

## 🛠️ Methodological Notes / Technical Specifications
* **Appliance Taxonomy:** Classified by time (deferrable/undeferrable) and power (adjustable/unadjustable). HVAC is modeled as undeferrable but power-adjustable.
* **Optimization Method:** Convex optimization formulated to schedule continuously adjustable inverter-based HVAC power consumption.
* **Unadjustable Load Generation:** Modeled as Poisson arrivals with uniform power demands ($0$ to $P_{\max}$) and exponential service durations.

## 💡 Personal Insights & Open Questions
* **Potential Application:** Designing device emulator profiles in EGoT. Creating separate virtual appliances for base unadjustable load (lights, computers) and adjustable HVAC loads enables EGoT to simulate realistic, dynamic demand response responses in OpenDSS.
* **Gap/Next Step:** The paper assumes continuously adjustable inverter HVAC technology; modeling legacy on-off (thermostatically controlled) HVAC systems using binary state models remains a challenge for real-world deployment.

## 📌 Critical Quotes
> "The optimal and sub-optimal algorithms can reduce the cost by about 25% and 10%, respectively... the power consumption PAR can be effectively reduced by the proposed algorithms, i.e., the total power consumption becomes more stable."
---
