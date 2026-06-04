# Literature Review Search Strings for EGoT PhD Dissertation

This document identifies areas in the dissertation draft [draft.md](file:///home/tylor/phd/draft.md) where additional literature can further strengthen the theoretical, physical, and cyber-physical arguments. It provides a step-by-step breakdown of these gaps and a database of academic search strings for Google Scholar, IEEE Xplore, and Scopus.

---

## 1. Step-by-Step Literature Review Analysis

### Step 1: ESI Concept, Standards, and Layered Decomposition
*   **Draft Context:** Sections 1.1 and 1.2 outline the NIST ESI definition and Grid Modernization Laboratory Consortium (GMLC) tenets, citing `brown_guide_2024` and `grid_modernization_laboratory_consortium_interoperability_2018`.
*   **Literature Needs:** Need to document the evolution of grid-boundary interface architectures (such as transactive energy nodes or VPP coordination hubs) and mathematical models of hierarchical layered decomposition in power grid optimization.
*   **Academic Target:** High-level power systems journals defining logical boundaries and transactive coordinate mechanisms.

### Step 2: Cyber-Physical Edge Security and Control Overrides
*   **Draft Context:** Section 1.2.2 describes how clients validate Volt-Var curves locally to reject destabilizing commands, citing `sarker_cyber-physical_2020` and `alsaid_privacy-preserving_2022`.
*   **Literature Needs:** Substantiate the physical consequences of compromised DER commands. We need papers describing how attackers can exploit secure communication protocols (like mTLS) by spoofing or hijacking utility controls to cause voltage/frequency collapse.
*   **Academic Target:** IEEE Transactions on Smart Grid, IEEE Transactions on Dependable and Secure Computing.

### Step 3: Privacy, Data Decoupling, and Load Shaping
*   **Draft Context:** Section 1.2.1 details smart meter privacy, citing `zeifman_nonintrusive_2011` (NILM) and `kement_privacy_2021` (reactive/real load shaping).
*   **Literature Needs:** Find studies analyzing the privacy threat of sub-minute telemetry, differential privacy in smart metering, and data isolation strategies in commercial utility databases.
*   **Academic Target:** Privacy Enhancing Technologies Symposium (POPETS), IEEE Transactions on Information Forensics and Security.

### Step 4: Ancillary Grid Services Formulations
*   **Draft Context:** Section 2 maps Energy, Reserve, Regulation, Frequency Response, Voltage Management, and Blackstart, citing `kolln_terms_2023`.
*   **Literature Needs:**
    *   *Reserve:* DER reserve capability rules and market designs (FERC Orders 841/2222).
    *   *Regulation:* Automatic Generation Control (AGC) tracking metrics and PJM market scoring rules.
    *   *Frequency Response:* NERC frequency response standards (BAL-001-2) and droop setting validation.
    *   *Voltage:* Smart inverter control loop oscillations ("hunting") under high-penetration solar.
    *   *Blackstart:* Grid-forming (GFM) control, cold load pickup (CLPU) inrush dynamics, and staggered switch restoration.
*   **Academic Target:** IEEE Transactions on Power Systems, IEEE Power and Energy Society General Meeting papers.

### Step 5: Smart Grid Protocol Overhead (REST vs. IoT)
*   **Draft Context:** Section 8 evaluates IEEE 2030.5 communication metrics against lightweight protocols, citing `slay_adoption_2018` and `slay_energy_2021`.
*   **Literature Needs:** Find papers comparing the throughput, latency, packet loss, and CPU load of XML-based REST protocols (HTTP) against binary or publish/subscribe IoT protocols (MQTT, CoAP, DDS) in utility applications.
*   **Academic Target:** IEEE Transactions on Industrial Informatics, IEEE Internet of Things Journal.

### Step 6: Measurement Uncertainty, State Estimation, and Topology Errors
*   **Draft Context:** Section 9.2 describes smart meter noise and topology mapping errors, citing `lin_credibility_2019`, `kong_estimation_2020`, and `luan_distribution_2013`.
*   **Literature Needs:** Document real-world smart meter calibration drift rates and phase-mapping identification algorithms using data analytics.
*   **Academic Target:** IEEE Transactions on Instrumentation and Measurement, IEEE Transactions on Power Delivery.

### Step 7: Future Extensions (DOL & Battery cycle Fade)
*   **Draft Context:** Section 10.2 proposes Dynamic Operating Limits (DOL) and battery degradation, citing `olympios_progress_2021`.
*   **Literature Needs:** Find mathematical models representing cycle-life and capacity fade of lithium-ion batteries under grid ancillary service dispatch, and thermal rating calculation methods for overhead lines.
*   **Academic Target:** Journal of Power Sources, IEEE Transactions on Energy Conversion.

---

## 2. Copy-Pasteable Search String Database

| Research Topic | Targeted Search Strings (Google Scholar / IEEE Xplore / Scopus) |
| :--- | :--- |
| **ESI Concepts & Decoupling** | `("Energy Service Interface" OR "transactive node") AND "customer-grid boundary" AND "decoupling"` |
| **Layered Grid Control** | `"layered decomposition" AND "hierarchical control" AND "distributed energy resources" AND "optimization"` |
| **NILM Privacy Threats** | `"Non-Intrusive Load Monitoring" AND "privacy threat" AND "smart meter" AND "occupancy detection"` |
| **Smart Meter Load Shaping** | `("load shaping" OR "load masking") AND "privacy" AND "energy storage" AND "reactive power"` |
| **Coordinated DER Attacks** | `("coordinated attack" OR "common-mode failure") AND "smart inverter" AND ("voltage collapse" OR "instability")` |
| **Edge Cyber Override** | `("local override" OR "fail-safe" OR "local validation") AND "smart inverter" AND ("malicious control" OR "cyber-physical")` |
| **Smart Grid SLAs & Negotiation** | `("WS-Agreement" OR "SLA") AND "smart grid" AND "contract negotiation" AND "transactive"` |
| **DR Baseline Errors & Gaming** | `"customer baseline load" AND ("estimation error" OR "gaming" OR "manipulation") AND "demand response"` |
| **DER Contingency Reserves** | `"contingency reserves" AND "distributed energy resources" AND ("aggregation" OR "ramp rate")` |
| **FERC Order 2222 Ancillary** | `"FERC Order 2222" AND "ancillary services" AND "aggregation" AND "battery storage"` |
| **PJM Regulation Score** | `"PJM" AND "regulation market" AND "performance score" AND ("correlation" OR "delay" OR "precision")` |
| **Frequency Response Verification** | `"primary frequency response" AND ("droop" OR "deadband") AND "smart inverter" AND ("validation" OR "compliance")` |
| **Smart Inverter Volt-Var Hunting** | `("Volt-Var" OR "Volt-Watt") AND "stability" AND "oscillation" AND "hunting" AND "smart inverter"` |
| **Grid-Forming Inverter Blackstart** | `"grid-forming" AND "inverter" AND ("blackstart" OR "islanded restoration" OR "voltage source")` |
| **Cold Load Pickup Mitigation** | `"cold load pickup" AND "mitigation" AND "microgrid" AND "staggered" AND "restoration"` |
| **IEEE 2030.5 CSIP Rules** | `"IEEE 2030.5" AND ("California Rule 21" OR "Common Smart Inverter Profile" OR "CSIP")` |
| **IEEE 2030.5 vs MQTT Footprint** | `("IEEE 2030.5" OR "SEP2") AND "MQTT" AND "performance comparison" AND ("overhead" OR "latency" OR "bandwidth")` |
| **EXI XML Performance** | `"Efficient XML Interchange" AND "smart grid" AND "performance" AND ("latency" OR "EXI")` |
| **Smart Meter Calibration Errors** | `"smart meter" AND ("calibration error" OR "measurement noise" OR "drift") AND "state estimation"` |
| **Topology Phase Mappings** | `"phase identification" AND "topology error correction" AND "smart meter" AND "voltage correlation"` |
| **Dynamic Operating Limits** | `"dynamic operating limits" AND "dynamic hosting capacity" AND "distribution network" AND "DER"` |
| **Battery Wear Cost Dispatch** | `"battery degradation" AND "cost function" AND "optimal power flow" AND "capacity fade"` |

---

## 3. Recommended Literature Survey Strategy

To systematically integrate papers found with these search strings:
1. **Reference Management:** Export the citations from Google Scholar or IEEE Xplore directly in BibTeX format and load them into a reference manager like Zotero or Mendeley.
2. **Key Venues:** Focus your search on high-impact journals, including:
   - *IEEE Transactions on Smart Grid*
   - *IEEE Transactions on Power Systems*
   - *IEEE Transactions on Sustainable Energy*
   - *IEEE Transactions on Industrial Informatics*
   - *Applied Energy*
3. **BibTeX Key Standard:** Ensure the BibTeX key format matches the convention in [bibfile.bib](file:///home/tylor/phd/dissertation/bibfile.bib) (e.g. `author_title_year`).
4. **Draft Updates:** When writing the dissertation main body files under [dissertation/MainMatter/](file:///home/tylor/phd/dissertation/MainMatter/), import these citations into the LaTeX code using the standard `\cite{key}` tags.
