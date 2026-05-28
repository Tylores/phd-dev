# The Open Distribution System Simulator (OpenDSS) Reference Guide | Project Pillar: Technical Specs
**Date:** May 2026
**Status:** Technical Documentation

## 🎯 Executive Summary
This manual is the official reference guide for the Open Distribution System Simulator (OpenDSS), an open-source, multi-phase electrical system simulation tool developed by the Electric Power Research Institute (EPRI). It details the program's design, script command syntax, COM interface, and modeling capabilities for analyzing modern electric utility distribution systems.

## 🔑 Key Arguments & Findings
* **Finding 1:** OpenDSS is built to handle unbalanced, multi-phase distribution network simulations, making it suitable for representing solar PV integration, battery storage, and dynamic grid assets.
* **Finding 2:** Its script-driven interface and COM API allow developers to programmatically control the power flow engine from third-party environments (such as Python, MATLAB, or Go), facilitating co-simulation and external controller testing.

## 🛠️ Methodological Notes / Technical Specifications
* **Software Version:** OpenDSS Revision 7.6.
* **Key Components:** Multi-phase line models, transformer models (e.g., autotransformers, GSU), capacitor banks, loads, and geomagnetic induced current (GIC) line models.
* **Execution Interface:** Command-line scripting, standalone GUI, and COM interface for external language bindings.

## 💡 Personal Insights & Open Questions
* **Potential Application:** This reference guide serves as the foundation for the OpenDSS co-simulations in this PhD project, where Go-based IEEE 2030.5 endpoints interact with a simulated utility grid controlled via Python scripts (`scripts/grid_services_sim.py`).
* **Gap/Next Step:** Direct real-time feedback loops between the EGoT REST services and the OpenDSS engine require careful synchronization of time steps, which is not covered in this steady-state simulation manual.

## 📌 Critical Quotes
> "The Open Distribution System Simulator (OpenDSS)"
> "Roger C. Dugan, Sr. Technical Executive, Electric Power Research Institute, Inc."
---
