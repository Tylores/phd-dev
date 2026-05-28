# Privacy-Preserving Information Security for the Energy Grid of Things | Project Pillar: Methodology
**Date:** May 2026
**Status:** Peer-Reviewed Literature

## 🎯 Executive Summary
This paper proposes a privacy-preserving, trust-augmented security scheme for the Energy Grid of Things (EGoT) smart grid platform. By applying the STRIDE threat modeling framework and utilizing data aggregation alongside randomized energy requests, the proposed architecture secures grid operations and protects customer privacy without the high computational overhead of homomorphic encryption.

## 🔑 Key Arguments & Findings
* **Finding 1:** Implementing smart grid standards (such as IEEE 2030.5 or OpenADR) without system-specific threat modeling can lead to highly complex systems with hidden, undetected security vulnerabilities.
* **Finding 2:** Customer load profile privacy in EGoT can be effectively preserved locally through data aggregation and randomized energy request obfuscation, which avoids the computational complexity of Homomorphic Encryption (HE) while still preventing behavioral pattern disclosure.

## 🛠️ Methodological Notes / Technical Specifications
* **Security Frameworks:** Threat modeling via STRIDE (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege) and vulnerability assessment via CVSS.
* **Trust Architecture:** Distributed Trust Model (DTM) consisting of a Central Distributed Trust Aggregator (CDTA) and Distributed Trust Model Clients (DTMC).
* **Privacy Protocols:** Localized load profiling, randomized energy request obfuscation, and data aggregation (contrasted with DLMS/COSEM and HE approaches).
* **Standard Integration:** Specifically targeted for IEEE 2030.5 and OpenADR-compliant environments.

## 💡 Personal Insights & Open Questions
* **Potential Application:** Direct architectural relevance to the security layer of the EGoT microservices fleet (e.g., mTLS configurations in the DCAP and EDevice services). It supports the design of the trust and identity modules for end-devices.
* **Gap/Next Step:** A quantitative evaluation of the security-utility tradeoff for the randomized energy requests is needed. Specifically, how much noise is introduced to grid service estimations, and can machine-learning-based non-intrusive load monitoring (NILM) still reconstruct user activities?

## 📌 Critical Quotes
> "Following industry standards with little understanding of the system to be developed may produce a complex system with undetected vulnerabilities."
> "In the EGoT smart grid implementation, we make use of data aggregation as a means of preserving privacy. ... Instead, we use randomized energy requests to obfuscate the user's behavioral patterns."
