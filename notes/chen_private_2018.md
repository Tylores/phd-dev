# Private Memoirs of IoT Devices: Safeguarding User Privacy in the IoT Era | Project Pillar: Literature Review
**Date:** June 2026
**Status:** Peer-Reviewed Literature

## 🎯 Executive Summary
This paper examines the privacy implications of cloud-connected IoT devices, demonstrating how seemingly harmless sensor telemetry leaks sensitive side-channel information. Focusing on smart energy systems, the authors show that solar PV generation profiles leak geographical location, and smart meter profiles leak occupancy and appliance usage, and they evaluate the trade-offs of using behind-the-meter batteries or thermal loads to mask these signatures.

## 🔑 Key Arguments & Findings
*   **Finding 1:** High-frequency solar generation data implicitly embeds geographical location (latitude and longitude) through day-length and solar noon characteristics, allowing location inference to within a few kilometers using public weather data.
*   **Finding 2:** Physical-layer data obfuscation (using behind-the-meter batteries or controllable thermal loads like electric water heaters) can distort load curves to prevent occupancy detection (reducing the Matthews Correlation Coefficient from 0.44 to 0.045), representing a clear trade-off between device cycle cost and privacy preservation.

## 🛠️ Methodological Notes / Technical Specifications
*   **Privacy Metrics:** Matthews Correlation Coefficient (MCC), Non-intrusive Occupancy Monitoring (NIOM), NILM disaggregation.
*   **Defenses Evaluated:** Differential privacy, Combined Heat and Privacy (CHPr), battery-based obfuscation, network traffic padding.
*   **IoT Devices Studied:** Smart meters, Enphase solar microinverters, Nest/Lyric smart thermostats.

## 💡 Personal Insights & Open Questions
*   **Potential Application:** Backs the EGoT threat model regarding privacy boundaries at the electrical point of connection, demonstrating that raw solar and load telemetry published to Mirror Usage Points (`/mup`) can leak physical location and habits, justifying aggregation and perturbation.
*   **Gap/Next Step:** The paper describes battery-based and thermal load obfuscation qualitatively, but does not formulate a closed-form economic optimization model that links battery cell degradation costs to the level of privacy achieved.

## 📌 Critical Quotes
> "Our recent work has demonstrated that solar generation data at a particular site also embeds the location of that site, and this location information can be extracted from the generation trace using solar analytics methods." (Page 1330)

> "A smart meter should provide usage information to a utility... but should do so in a way that prevents occupancy or NILM-based analytics from being performed on the data." (Page 1334)
---
