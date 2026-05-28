# Customer Classification and Load Profiling Method for Distribution Systems | Project Pillar: Methodology
**Date:** May 2026
**Status:** Peer-Reviewed Literature

## 🎯 Executive Summary
This paper proposes an automated customer classification and load profiling method using the ISODATA clustering algorithm applied to hourly automatic meter reading (AMR) data. It addresses limitations of static customer information system (CIS) classification by including outlier filtering and temperature dependency corrections, demonstrating its effectiveness on a dataset of 660 customers in Finland.

## 🔑 Key Arguments & Findings
* **Finding 1:** Traditional customer classification in DSOs is based on static, outdated questionnaires from customer contracts, leading to significant classification errors due to changes in heating systems or appliance additions.
* **Finding 2:** High-volume, dynamic AMR data allows clustering algorithms like ISODATA to group customers based on real, multi-temporal consumption patterns, significantly improving the accuracy of low-voltage distribution network state estimation.

## 🛠️ Methodological Notes / Technical Specifications
* **Algorithms:** ISODATA (Iterative Self-Organizing Data Analysis Technique) compared against K-means clustering.
* **Correction & Filtering:** Temperature dependency correction and statistical outlier filtering.
* **Testing Bounds:** Demonstrated on a dataset of 660 hourly metered customers in Finland.
* **Software Tools:** LoadModellerPRO program (developed by VTT, Finland) and MATLAB environment.

## 💡 Personal Insights & Open Questions
* **Potential Application:** Apply consumption-based clustering (e.g., ISODATA) on EGoT endpoints' telemetry (from Mirror Usage Points) to automatically categorize DER loads for precise local grid services simulation.
* **Gap/Next Step:** How do these legacy load profiles adapt to active distribution network scenarios where customer behavior is dynamically modified by active demand response and real-time smart inverter controls?

## 📌 Critical Quotes
> "Now that the automatic meter-reading systems are becoming more common, customer classiﬁcation and load proﬁling could be done according to actual consumption data."
> "This paper proposes the use of the ISODATA algorithm for customer classiﬁcation. The proposed customer classiﬁcation and load proﬁling method also includes temperature dependency correction and outlier ﬁltering."
