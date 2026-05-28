# Coordinated Use of Smart Inverters With Legacy Voltage Regulating Devices in Distribution Systems With High Distributed PV Penetration—Increase CVR Energy Savings | Project Pillar: Methodology
**Date:** May 2026
**Status:** Peer-Reviewed Literature

## 🎯 Executive Summary
This paper presents two voltage optimization methodologies to coordinate smart inverters with legacy voltage-regulating devices (e.g., load tap changers and capacitor banks) to enhance energy savings from Conservation Voltage Reduction (CVR). Tested on utility distribution systems, the coordinated approach shows an additional 0.3% to 0.9% energy savings compared to using legacy devices alone, while successfully maintaining grid voltages within ANSI limits.

## 🔑 Key Arguments & Findings
* **Finding 1:** Static legacy voltage-regulating devices can be paired with smart inverters to manage secondary voltage profiles dynamically, enabling deeper voltage reductions for CVR without violating the lower ANSI voltage limit of 0.95 p.u.
* **Finding 2:** Two modes of smart inverter operation—autonomous volt/VAR control and aggregated reactive power control—are developed, showing that autonomous mode requires significantly less communication infrastructure while still providing substantial CVR benefits.

## 🛠️ Methodological Notes / Technical Specifications
* **Software Tools:** OpenDSS utility system models for feeder simulation.
* **Controls Simulated:** Autonomous Volt/VAR control (based on local voltage feedback) and Aggregated reactive power control (centralized dispatch).
* **Load Modeling:** Exponential load model using active/reactive Conservation Voltage Reduction (CVR) factors.
* **Operational Constraints:** ANSI C84.1-2011 limits (0.95 to 1.05 p.u.) and line thermal constraints.

## 💡 Personal Insights & Open Questions
* **Potential Application:** The coordinated control strategies can be modeled in EGoT's OpenDSS integration scripts (`scripts/grid_services_sim.py`) to simulate how EGoT devices executing DER programs interact with simulated utility LTCs.
* **Gap/Next Step:** The paper does not analyze the impact of high-frequency solar variability (cloud transients) on the wear-and-tear of mechanical tap changers when smart inverters switch modes rapidly.

## 📌 Critical Quotes
> "Simulation results demonstrate that the proposed algorithms can achieve around 1.8%–3.6% energy savings when only using legacy voltage regulating devices and an additional 0.3%–0.9% when adding smart inverters."
> "With the development of PV inverters and the requirements of PV interconnection standards, smart inverter has been widely adopted by PV system vendors..."
---
