# Adoption of an Internet of Things Framework for Distributed Energy Resource Coordination and Control | Project Pillar: Methodology
**Date:** May 2026
**Status:** Peer-Reviewed Literature

## 🎯 Executive Summary
This Master's thesis investigates the feasibility and performance of adopting an open-source Internet of Things (IoT) framework (specifically AllJoyn) to facilitate distributed energy resource (DER) coordination and control. It develops a testbed using C++ client applications to assess communication latency, network overhead, and system resource utilization during scaling.

## 🔑 Key Arguments & Findings
* **Finding 1:** Leveraging existing consumer IoT frameworks allows for rapid deployment, device discovery, and interoperability among heterogeneous DER devices without building custom communication stacks from scratch.
* **Finding 2:** System resource utilization (CPU, memory) and network bandwidth scale predictably with the number of concurrent device connections, indicating that lightweight messaging models are essential for resource-constrained edge devices in grid operations.

## 🛠️ Methodological Notes / Technical Specifications
* **Software Framework:** AllJoyn IoT framework.
* **Implementation Language:** C++ (spawning multiple Distribution Management System - DMS clients in tmux sessions).
* **Monitoring Tools:** `tshark` for network packet analysis, and shell scripts parsing CPU load and memory usage (`free`, `top`).

## 💡 Personal Insights & Open Questions
* **Potential Application:** Understand EGoT's developmental lineage. The architecture evolved from early collaborative IoT frameworks (like AllJoyn/IoTivity) to standard-compliant IEEE 2030.5 REST/Go microservices.
* **Gap/Next Step:** As AllJoyn has been deprecated, the thesis leaves open how the architectural concepts of peer discovery and low-overhead RPC map onto formal utility standards like IEEE 2030.5.

## 📌 Critical Quotes
> "Adoption of an Internet of Things Framework for Distributed Energy Resource Coordination and Control"
---
