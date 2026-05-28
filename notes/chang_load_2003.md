# Load profiling and its applications in power market | Project Pillar: Methodology
**Date:** May 2026
**Status:** Peer-Reviewed Literature

## 🎯 Executive Summary
This paper presents a customer load profiling and assignment methodology for retail electricity markets designed to avoid the high capital cost of installing interval meters. The authors develop a two-step framework utilizing Fuzzy C-Means (FCM) clustering to identify typical load shapes and a C4.5 decision tree classifier to assign customers to these profiles using monthly energy billing data.

## 🔑 Key Arguments & Findings
* **Finding 1:** High-resolution interval meters are cost-prohibitive for universal deployment; instead, load profiling using readily available monthly energy consumption records provides a reliable alternative for customer screening and tariff scheduling.
* **Finding 2:** A machine-learning approach using Fuzzy C-Means clustering combined with a Gain-Ratio-based decision tree successfully classifies Taiwan Power Company customer profiles with an average test accuracy of 86.7%.

## 🛠️ Methodological Notes / Technical Specifications
* **Clustering Method:** Fuzzy C-Means (FCM) clustering to generate per-unit representative load profiles.
* **Classification Model:** C4.5 Decision Tree classifier based on Gain-Ratio split metrics.
* **Feature Engineering:** Ratios of monthly energy usages ($E_1$), monthly usage differences ($E_2$), seasonal usage ratios ($E_3$), and seasonal usage averages ($E_4$).
* **Dataset:** 15-minute active and reactive power metered data and billing records from 500 customers of Taiwan Power Company (TPC).

## 💡 Personal Insights & Open Questions
* **Potential Application:** The Fuzzy C-Means and decision-tree profiling approach can be used by the EGoT Mirror Usage Point (MUP) service to fill in missing telemetry data or to classify new devices (via EDevice) when high-resolution smart meter readings are unavailable.
* **Gap/Next Step:** The study uses historical monthly billing data which assumes static load behavior. The method needs to be evaluated under modern scenarios with distributed energy resources (DERs like batteries and solar PV) where behind-the-meter generation changes the net monthly consumption.

## 📌 Critical Quotes
> "At the present time, requiring a meter as a prerequisite for power customers to choose a power supplier is not yet achievable."
> "Test results indicate that the decision tree method are capable of assigning customer load profiles, or at least, performing a preliminary class screenings."
