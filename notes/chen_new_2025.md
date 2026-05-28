# A New Electronic Voltage Transformer Applicable to AMI Smart Meters | Project Pillar: Technical Specs
**Date:** May 2026
**Status:** Peer-Reviewed Literature

## 🎯 Executive Summary
This paper introduces a modular Electronic Voltage Transformer (EVT) design suitable for AMI smart meters. Utilizing high-precision resistive voltage dividers and a push-pull power amplifier, the proposed modular EVT can be configured for various distribution voltage levels (380 V, 11.4 kV, 22.8 kV) to output a stable 114 V that provides both high-accuracy voltage measurement (meeting IEC 60044-7 Class 0.1) and the power required to drive the smart meter.

## 🔑 Key Arguments & Findings
* **Finding 1:** Traditional electromagnetic VTs are bulky, heavy, susceptible to magnetic saturation and resonance, and are prone to insulation degradation and explosion risks due to uneven epoxy grouting and partial discharges.
* **Finding 2:** Combining a push-pull power amplifier with high-precision resistive voltage dividers allows the EVT to output enough power to handle the high startup currents of AMI smart meters without causing significant thermal drift, maintaining high accuracy.

## 🛠️ Methodological Notes / Technical Specifications
* **Components:** Caddock Ultra-Stable Low TC Film Resistors (0.01% tolerance, 5 ppm/°C temperature coefficient) configured in series (e.g., ten 100-kΩ resistors for the 380 V module).
* **Power Amplifier:** High-precision push-pull power amplifier circuit for impedance matching and load-driving capabilities.
* **Tested Ratings:** 380 V/114 V modular step-down; scalable to 11.4 kV/114 V and 22.8 kV/114 V via cascaded modules.
* **Standard Met:** Class 0.1 measurement accuracy according to IEC standard 60044-7.

## 💡 Personal Insights & Open Questions
* **Potential Application:** In EGoT implementation, this provides technical specifications for the design and selection of voltage sensors in the End Device (EDevice) emulation and Metering (MUP) networks, ensuring safe and lightweight deployment of physical testbed meters.
* **Gap/Next Step:** The experimental validation is focused on a 380 V/114 V application under standard grid frequencies. Testing the performance, harmonic distortion, and frequency response of the cascaded high-voltage modules (11.4 kV and 22.8 kV) under transient and faulty grid conditions is a necessary next step.

## 📌 Critical Quotes
> "Compared with the traditional VT, the EVT has no iron core structure, so there is no problem with iron core magnetic saturation and ferromagnetic resonance."
> "The experimental results show that the new EVT for the 380 V/114 V application not only successfully drives the AMI smart meter, but also meets the Class 0.1 according to IEC standard 60044-7."
