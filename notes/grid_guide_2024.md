# Guide to Developing Energy Services Interfaces | Project Pillar: Technical Specs
**Date:** May 2026
**Status:** Technical Documentation

## 🎯 Executive Summary
This technical guide (PNNL-35111), prepared by a multi-laboratory consortium including PNNL, LBNL, NREL, ANL, and ORNL, provides a comprehensive framework for designing and implementing Energy Services Interfaces (ESIs). It details the functional, logical, and security requirements to support secure, bi-directional interactions between customer-owned energy assets and external grid operators or aggregators.

## 🔑 Key Arguments & Findings
* **Finding 1:** An ESI is a critical facility-boundary gateway that decouples internal building/industrial DER operations from external grid service providers, protecting customer privacy and local control while satisfying grid dispatch requests.
* **Finding 2:** Standardizing ESI architecture is essential for grid interoperability, requiring structured methods for device discovery, capability advertisements, flow reservation, and telemetry mapping using industry protocols such as IEEE 2030.5.

## 🛠️ Methodological Notes / Technical Specifications
* **Document Reference:** PNNL-35111, sponsored by the U.S. Department of Energy.
* **Collaborating Institutions:** Lawrence Berkeley National Laboratory (LBNL), Pacific Northwest National Laboratory (PNNL), National Renewable Energy Laboratory (NREL), Argonne National Laboratory (ANL), and Oak Ridge National Laboratory (ORNL).
* **Architectural Boundaries:** Customer facility boundary, bi-directional service-oriented logical interfaces, grid-side vs. customer-side decoupling.

## 💡 Personal Insights & Open Questions
* **Potential Application:** EGoT is a direct implementation of an ESI platform, specifically leveraging the IEEE 2030.5 standard to establish the boundary. The microservices `DCAP`, `EDevice`, and `FlowReservation` implement the ESI capability advertisement and scheduling concepts defined in this guide.
* **Gap/Next Step:** The guide defines abstract ESI interactions; mapping these logical transactions to physical device protocols (e.g., translating IEEE 2030.5 REST commands to Modbus register writes) at the edge is left to system developers and needs standardized translation layers.

## 📌 Critical Quotes
> "Guide to Developing Energy Services Interfaces"
> "PNNL-35111... January 2024"
---
