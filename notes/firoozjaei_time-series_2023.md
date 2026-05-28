# Time-Series Load Data Analysis for User Power Profiling | Project Pillar: Methodology
**Date:** May 2026
**Status:** Peer-Reviewed Literature

## 🎯 Executive Summary
This paper introduces a user power profiling methodology that utilizes the Dynamic Time Warping (DTW) clustering algorithm to analyze time-series load data from smart meters. Evaluated on the minutely AMPds2 residential dataset, the model demonstrates a true positive rate of up to 90.91% for load pattern identification while highlighting the associated user privacy vulnerabilities.

## 🔑 Key Arguments & Findings
* **Finding 1:** Traditional Euclidean Distance (ED) fails to match similar load profiles when slight time delays or shifts occur, whereas Dynamic Time Warping (DTW) is invariant to signal warping and time distortion, allowing robust phase-shifted pattern recognition.
* **Finding 2:** While fine-grained power profiling enables accurate demand-response (DR) forecasting and fault detection, it presents severe privacy risks by allowing external entities to infer specific in-home activities and appliance operating cycles.

## 🛠️ Methodological Notes / Technical Specifications
* **Key Algorithms:** Dynamic Time Warping (DTW) via Dynamic Programming (DP), Euclidean Distance (ED).
* **Reference Dataset:** Almanac of Minutely Power dataset version 2 (AMPds2) (2 years of minutely electricity, water, and gas readings from a Greater Vancouver home).
* **Target Application:** Load type clustering, anomaly/theft detection, and Non-Intrusive Load Monitoring (NILM) analysis.
* **Performance:** Achieved a 90.91% true positive rate (TPR) for load type clustering.

## 💡 Personal Insights & Open Questions
* **Potential Application:** The DTW metric can be implemented in the EGoT Mirror Usage Point (MUP) or telemetry export functions to classify customer load profiles dynamically, aiding in custom tariff or DER control optimization.
* **Gap/Next Step:** Because DTW is computationally expensive ($O(N \cdot M)$) and sequential (non-parallelizable), finding ways to scale this classification to run efficiently on thousands of edge devices or within real-time EGoT web servers remains an open challenge.

## 📌 Critical Quotes
> "Dynamic time warping (DTW) is selected to measure the similarity between the power usage time series due to its properties, i.e., signal warping invariability and implementation simplicity."
> "Normally, consumers are clustered based on their load curves... By recognizing the load patterns of a new consumer, he/she is classified into a particular consumer group..."
---
