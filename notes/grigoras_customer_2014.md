# Customer classification and load profiling using data from Smart Meters | Project Pillar: Methodology
**Date:** May 2026
**Status:** Peer-Reviewed Literature

## 🎯 Executive Summary
This paper describes a methodology that utilizes Kohonen Self-Organizing Maps (SOMs) to classify distribution grid customers and generate Typical Load Profiles (TLPs). By grouping residential consumers based on simple aggregate metrics (daily energy consumption, minimum load, and maximum load), the proposed unsupervised learning model reduces substation load estimation errors to 2.14%, outperforming classical clustering techniques.

## 🔑 Key Arguments & Findings
* **Finding 1:** High-resolution smart meter installations generate a massive data flow that requires robust Meter Data Management Systems (MDMS) but unlocks significant opportunities for grid optimization, line loss reduction, and state estimation.
* **Finding 2:** Self-Organizing Maps provide an effective way to project multidimensional consumer data into lower dimensions while preserving topology, enabling robust customer classification even when detailed physical information about the grid nodes is poor.

## 🛠️ Methodological Notes / Technical Specifications
* **Key Algorithm:** Kohonen Self-Organizing Maps (SOMs), using unsupervised learning, winner-take-all competitive adaptation, and Euclidean norm distance metrics.
* **Input Parameters:** Daily (or monthly) energy consumption, minimum active power load, and maximum active power load.
* **Validation Context:** Household consumers in a rural distribution system.
* **Accuracy:** Decreased average substation hourly load estimation error from 3.85% (for standard clustering) to 2.14%.

## 💡 Personal Insights & Open Questions
* **Potential Application:** The typical load profiling approach can be utilized in EGoT to generate realistic mock telemetry for Mirror Usage Points (MUPs) and to model customer baseline loads in the OpenDSS simulator when historical micro-level data is unavailable.
* **Gap/Next Step:** The method relies on static inputs (daily energy, min/max load). How the Kohonen map adapts to dramatic shifts in consumer behaviors over time (e.g., after installing rooftop PV or purchasing an EV) requires dynamic re-clustering.

## 📌 Critical Quotes
> "Self-organizing techniques are extremely useful for assisting the electric distribution services providers in the process of customers’ classification on the basis of electrical characteristics (daily/monthly energy consumption, minimum load, and maximum load)."
> "The comparison with the results obtained with a clustering based approach... indicated a decrease of average estimation error from 3.85 % to 2.14 %..."
---
