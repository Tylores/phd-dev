# Cyber-Physical Security and Resiliency Analysis Testbed for Critical Microgrids with IEEE 2030.5 | Project Pillar: Methodology
**Date:** May 2026
**Status:** Peer-Reviewed Literature

## 🎯 Executive Summary
This paper presents a co-simulation testbed combining the IEEE 2030.5 protocol with the OpenDSS distribution system simulator via a REST interface to analyze cyber-physical security. The resiliency of the Miramar military microgrid is evaluated under coordinated physical and cyber-attacks that exploit smart inverter reactive power controls.

## 🔑 Key Arguments & Findings
* **Finding 1:** Malicious control signals sent via the IEEE 2030.5 protocol (e.g., setting inappropriate VAR curve configurations) can cause complete voltage collapse in islanded microgrids due to a lack of alternative reactive power support.
* **Finding 2:** Calculating real-time resiliency scores improves the situational awareness of grid operators, enabling them to make proactive adjustments such as disconnecting remote DER controls to prevent cyber-attacks from escalating.

## 🛠️ Methodological Notes / Technical Specifications
* **Simulators & Protocols:** OpenDSS distribution system simulator, IEEE 2030.5 (REST protocol and Common Smart Inverter Profile - CSIP).
* **Test System:** Model of the Miramar military microgrid.
* **Resiliency Tools:** CyPhyR (a cyber-physical analysis tool for measuring and enabling resiliency in microgrids).

## 💡 Personal Insights & Open Questions
* **Potential Application:** Informing the integration of security mechanisms and anomaly detection in EGoT's Go-based microservices, particularly validating how malicious DER control commands sent over IEEE 2030.5 impact physical feeder simulations in OpenDSS.
* **Gap/Next Step:** The paper focuses on the impacts of compromised commands but does not analyze how to secure the IEEE 2030.5 infrastructure itself, such as the configuration and overhead of mutual TLS (mTLS) which is standard-mandated.

## 📌 Critical Quotes
> "Now if the attacker sends malicious control signals to the DER units by exploiting the IEEE 2030.5 protocol and sets them up for inappropriate VAR support, the islands will collapse immediately as there is not enough sources in the system to stabilize the system."
---
