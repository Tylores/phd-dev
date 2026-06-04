# Avoiding Occupancy Detection From Smart Meter Using Adversarial Machine Learning | Project Pillar: Literature Review
**Date:** June 2026
**Status:** Peer-Reviewed Literature

## 🎯 Executive Summary
This paper introduces the Adversarial Machine Learning Occupancy Detection Avoidance (AMLODA) framework, which injects optimal noise to smart meter profiles to mask occupancy signatures. The framework is designed to prevent LSTM-based privacy disaggregation attacks while preserving billing accuracy under Time-of-Use (TOU) and Peak-Load Pricing (PLP) tariffs.

## 🔑 Key Arguments & Findings
*   **Finding 1:** High-frequency smart meter readings leak sensitive household occupancy signatures. Using Recurrent Neural Networks (specifically LSTMs), adversaries can identify occupancy with up to 92-99% accuracy.
*   **Finding 2:** Adding a zero-mean data perturbation that cancels out every 2 seconds masks occupancy signatures (making LSTM predictions close to a random guess) without altering cumulative energy usage, thus preserving billing correctness.

## 🛠️ Methodological Notes / Technical Specifications
*   **Models & Tools:** LSTM neural networks, PyTorch, Gradient Descent optimization.
*   **Dataset:** ETH Zurich Electricity Consumption and Occupancy (ECO) dataset.
*   **Evaluation Metrics:** Matthews Correlation Coefficient (MCC) and Area Under the ROC Curve (AUC).

## 💡 Personal Insights & Open Questions
*   **Potential Application:** Directly supports the privacy pillar of the EGoT platform, confirming the necessity of database decoupling and illustrating that high-resolution data should be obfuscated before being exposed to utility billing engines.
*   **Gap/Next Step:** The proposed data perturbation is software-based and requires smart meters to execute gradient computation in real-time. The feasibility and computational overhead on low-power edge microcontrollers are not analyzed.

## 📌 Critical Quotes
> "The proposed privacy-preserving framework is designed to mask real-time or near real-time electricity usage information using calculated optimum noise without compromising users’ billing systems functionality." (Page 35411)

> "Our proposed AMLODA model uses optimum noise added to or subtracted from the meter data such that the adversary receives scrambled data without using any cryptographic keys." (Page 35414)
---
