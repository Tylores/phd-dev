# Load profiling and data mining techniques in electricity deregulated market | Project Pillar: Methodology
**Date:** May 2026
**Status:** Peer-Reviewed Literature

## 🎯 Executive Summary
This paper reviews and compares load profiling methods and data mining techniques (such as KDD, classification, and clustering) used in deregulated electricity markets. It proposes a customer classification framework that leverages historical customer consumption data to detect anomalies, faulty metering, billing errors, and potential non-technical losses.

## 🔑 Key Arguments & Findings
* **Finding 1:** In deregulated electricity markets, understanding dynamic customer consumption and billing transaction patterns is critical for distribution companies to design dedicated tariffs and marketing strategies.
* **Finding 2:** Unlike standard data pre-processing where abnormal data/outliers are routinely discarded or smoothed, this study deliberately targets abnormal data as outliers to identify non-technical losses (electricity theft, fraud, faulty metering, billing errors).

## 🛠️ Methodological Notes / Technical Specifications
* **Procedures:** Knowledge Discovery in Databases (KDD), classification, and clustering.
* **Metrics of Adequacy:** Mean Index of Adequacy (MIA) for cluster compactness, Clustering Dispersion Indicator (CDI) for cluster separation (referencing studies in Portugal).
* **Testing Bounds:** Customer historical database from an unnamed utility company.

## 💡 Personal Insights & Open Questions
* **Potential Application:** The framework of mapping typical daily/weekly load profile baselines and flagging deviations as potential anomalies can be implemented in the EGoT Mirror Usage Point (MUP) microservice. This can serve as a real-time sanity check for end-device status before telemetry is exported to grid simulators.
* **Gap/Next Step:** The paper focuses on comparative analysis of classification and clustering methods but does not implement the actual detection model, leaving the prediction of non-technical losses to a subsequent paper.

## 📌 Critical Quotes
> "The objective of this study is to determine the best load profiling methods and data mining techniques to classify, detect and predict non-technical losses in the distribution sector..."
> "...during the data pre-processing phase, most abnormal data is removed or replaced... however, in this study, the abnormal data is going to be treated as outliers, in order to discover abnormalities or irregularities."
