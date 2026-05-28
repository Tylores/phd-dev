# EGoT PhD Project Literature Review and Gap Analysis

This document compiles the academic literature landscaping, gap analysis, and proposed review outline for the **Energy Grid of Things (EGoT)** PhD dissertation research, as requested in [landscaping.md](file:///home/tylor/phd/landscaping.md). It has been updated to incorporate the GMLC Common Grid Services definitions and ESI lifecycle mapping reviews.

---

# Phase 1: Literature Landscape Mapping

This section maps the academic literature landscape across five primary themes that intersect with the EGoT system design, highlighting conflicting viewpoints and technical methodologies.

## Theme 1: Interoperability Standards and Protocols for Distributed Energy Resources (DER)
This theme covers the standardized protocols and communication interfaces used to integrate DERs into utility networks, primarily focusing on IEEE 2030.5 (SEP 2.0), IEEE 1547, OpenADR, Modbus, and DNP3.

### Primary Sources
* [alsaid_privacy-preserving_2022.md](file:///home/tylor/phd/notes/alsaid_privacy-preserving_2022.md)
* [johnson_evaluation_2021.md](file:///home/tylor/phd/notes/johnson_evaluation_2021.md)
* [slay_adoption_2018.md](file:///home/tylor/phd/notes/slay_adoption_2018.md)
* [slay_energy_2021.md](file:///home/tylor/phd/notes/slay_energy_2021.md)
* [grid_guide_2024.md](file:///home/tylor/phd/notes/grid_guide_2024.md)
* [widergren_plug-and-play_2019.md](file:///home/tylor/phd/notes/widergren_plug-and-play_2019.md)
* [sarker_cyber-physical_2020.md](file:///home/tylor/phd/notes/sarker_cyber-physical_2020.md)
* [obi_distributed_2020.md](file:///home/tylor/phd/notes/obi_distributed_2020.md)

### Conflicting Viewpoints
* **Protocol Weight vs. Semantic Modeling:** [slay_adoption_2018.md](file:///home/tylor/phd/notes/slay_adoption_2018.md) argues that full IEEE 2030.5 XML-based REST APIs are too heavy and computationally expensive for low-power edge microcontrollers, advocating for lightweight IoT protocols like MQTT. Conversely, [slay_energy_2021.md](file:///home/tylor/phd/notes/slay_energy_2021.md) and [grid_guide_2024.md](file:///home/tylor/phd/notes/grid_guide_2024.md) assert that the comprehensive semantic resource schemas and built-in mTLS features of IEEE 2030.5 are essential to construct a secure and interoperable Energy Service Interface (ESI) boundary.
* **Standard-Compliance vs. Hidden Vulnerabilities:** [widergren_plug-and-play_2019.md](file:///home/tylor/phd/notes/widergren_plug-and-play_2019.md) frames standard compliance as a complete solution for DER integration. In contrast, [alsaid_privacy-preserving_2022.md](file:///home/tylor/phd/notes/alsaid_privacy-preserving_2022.md) and [sarker_cyber-physical_2020.md](file:///home/tylor/phd/notes/sarker_cyber-physical_2020.md) argue that implementing standard schemas without system-specific threat modeling introduces hidden vulnerabilities (e.g., identity spoofing, command modification) that threaten physical grid stability.
* **Paper-Certified vs. Practical Interoperability:** [johnson_evaluation_2021.md](file:///home/tylor/phd/notes/johnson_evaluation_2021.md) highlights that although devices are certified to standards like IEEE 1547.1 using SunSpec Modbus or DNP3, laboratory testing reveals significant discrepancies in vendor implementations, parameter mapping offsets, and response latencies that require active software-layer adjustment.

---

## Theme 2: Smart Inverter Control and Voltage Management (Volt-Var / Volt-Watt)
This theme addresses the use of smart inverters to provide reactive and active power support (Volt-Var and Volt-Watt curves) to regulate voltages and increase hosting capacity on distribution feeders.

### Primary Sources
* [bello_optimal_2017.md](file:///home/tylor/phd/notes/bello_optimal_2017.md)
* [iioka_appropriate_2022.md](file:///home/tylor/phd/notes/iioka_appropriate_2022.md)
* [dharmawardena_distributed_2022.md](file:///home/tylor/phd/notes/dharmawardena_distributed_2022.md)
* [ding_coordinated_2023.md](file:///home/tylor/phd/notes/ding_coordinated_2023.md)
* [ding_photovoltaic_2016.md](file:///home/tylor/phd/notes/ding_photovoltaic_2016.md)
* [smith_analysis_2016.md](file:///home/tylor/phd/notes/smith_analysis_2016.md)
* [azzolini_analysis_2022.md](file:///home/tylor/phd/notes/azzolini_analysis_2022.md)
* [lee_optimal_2020.md](file:///home/tylor/phd/notes/lee_optimal_2020.md)
* [lee_adopting_2023.md](file:///home/tylor/phd/notes/lee_adopting_2023.md)

### Conflicting Viewpoints
* **Autonomous Local Curves vs. Centralized Optimization:** [bello_optimal_2017.md](file:///home/tylor/phd/notes/bello_optimal_2017.md) and [iioka_appropriate_2022.md](file:///home/tylor/phd/notes/iioka_appropriate_2022.md) show that static, local autonomous Volt-VAR curves require no communications and effectively regulate local voltages. However, [dharmawardena_distributed_2022.md](file:///home/tylor/phd/notes/dharmawardena_distributed_2022.md) and [smith_analysis_2016.md](file:///home/tylor/phd/notes/smith_analysis_2016.md) argue that static local curves are suboptimal and can trigger control "hunting" or voltage oscillations under high PV variability. They advocate for dynamically updated curves optimized by cellular networks or central dispatchers.
* **Coordination with Legacy Infrastructure:** [ding_coordinated_2023.md](file:///home/tylor/phd/notes/ding_coordinated_2023.md) argues that smart inverter controls must be actively coordinated with legacy utility voltage regulators and load tap changers (LTC) to prevent tap wear-out. Other works, such as [fiorelli_how_2013.md](file:///home/tylor/phd/notes/fiorelli_how_2013.md) and [lee_optimal_2020.md](file:///home/tylor/phd/notes/lee_optimal_2020.md), analyze inverter curve parameters in isolation without addressing coordination with legacy mechanical devices.
* **Reactive Power Modeling Assumptions:** [azzolini_analysis_2022.md](file:///home/tylor/phd/notes/azzolini_analysis_2022.md) points out that assuming a constant power factor for distribution loads leads to significant errors in Volt-VAR optimization results, whereas many load flow studies assume flat power factors due to a lack of per-phase reactive telemetry.

---

## Theme 3: Load Profiling, Customer Segmentation, and Advanced Metering Infrastructure (AMI)
This theme focuses on analyzing smart meter data to segment customers, detect network anomalies, estimate topology, and support demand response programs.

### Primary Sources
* [chang_load_2003.md](file:///home/tylor/phd/notes/chang_load_2003.md)
* [mutanen_customer_2011.md](file:///home/tylor/phd/notes/mutanen_customer_2011.md)
* [grigoras_customer_2014.md](file:///home/tylor/phd/notes/grigoras_customer_2014.md)
* [firoozjaei_time-series_2023.md](file:///home/tylor/phd/notes/firoozjaei_time-series_2023.md)
* [wang_load_2015.md](file:///home/tylor/phd/notes/wang_load_2015.md)
* [deboever_impact_2020.md](file:///home/tylor/phd/notes/deboever_impact_2020.md)
* [luan_distribution_2013.md](file:///home/tylor/phd/notes/luan_distribution_2013.md)
* [lin_credibility_2019.md](file:///home/tylor/phd/notes/lin_credibility_2019.md)
* [kong_estimation_2020.md](file:///home/tylor/phd/notes/kong_estimation_2020.md)

### Conflicting Viewpoints
* **Statistical Clustering vs. Deep Learning Models:** [chang_load_2003.md](file:///home/tylor/phd/notes/chang_load_2003.md) and [mutanen_customer_2011.md](file:///home/tylor/phd/notes/mutanen_customer_2011.md) leverage classical K-means and Fuzzy C-means clustering due to their computational simplicity and explainability. In contrast, [firoozjaei_time-series_2023.md](file:///home/tylor/phd/notes/firoozjaei_time-series_2023.md) argues that traditional clustering fails to capture multi-scale temporal dynamics and non-linearities, proposing deep learning (RNN/LSTM/DRL) to model user load profiles and detect measurement anomalies.
* **Data Granularity Requirements:** [deboever_impact_2020.md](file:///home/tylor/phd/notes/deboever_impact_2020.md) demonstrates that 60-minute data fails to capture voltage violations and peak loads in quasi-static simulations, proving that sub-15-minute data is required. Conversely, privacy research warns that high-frequency smart meter readings expose customer behavioral patterns, arguing that utilities should only store aggregated hourly or daily profiles.
* **Topology Accuracy Assumptions:** While most load profiling and state estimation literature assumes a perfect GIS topology model, [luan_distribution_2013.md](file:///home/tylor/phd/notes/luan_distribution_2013.md) demonstrates that GIS databases often contain phase and transformer mapping errors, proposing data-driven voltage correlation analysis to identify and correct these errors.

---

## Theme 4: Data Privacy, Security, and Trust Boundaries
This theme deals with protecting customer data privacy, defending against cyber-physical attacks, and establishing trust verification boundaries between end-user devices and energy services.

### Primary Sources
* [alsaid_privacy-preserving_2022.md](file:///home/tylor/phd/notes/alsaid_privacy-preserving_2022.md)
* [ibrahem_privacy_2021.md](file:///home/tylor/phd/notes/ibrahem_privacy_2021.md)
* [kement_privacy_2021.md](file:///home/tylor/phd/notes/kement_privacy_2021.md)
* [fernando_developing_2021.md](file:///home/tylor/phd/notes/fernando_developing_2021.md)
* [quinn_privacy_2009.md](file:///home/tylor/phd/notes/quinn_privacy_2009.md)
* [ruddell_guidance_2020.md](file:///home/tylor/phd/notes/ruddell_guidance_2020.md)
* [sarker_cyber-physical_2020.md](file:///home/tylor/phd/notes/sarker_cyber-physical_2020.md)

### Conflicting Viewpoints
* **Homomorphic Encryption vs. Local Obfuscation:** [ibrahem_privacy_2021.md](file:///home/tylor/phd/notes/ibrahem_privacy_2021.md) advocates for homomorphic encryption (HE) as the ultimate solution for secure smart meter billing data transmission. In contrast, [alsaid_privacy-preserving_2022.md](file:///home/tylor/phd/notes/alsaid_privacy-preserving_2022.md) and [kement_privacy_2021.md](file:///home/tylor/phd/notes/kement_privacy_2021.md) point out that HE is computationally too heavy for low-power edge meters, recommending local randomized energy requests, data aggregation, or battery load-shaping as more practical options.
* **Behavioral Trust Scores vs. Performance-Based Settlement:** [fernando_developing_2021.md](file:///home/tylor/phd/notes/fernando_developing_2021.md) proposes a multi-layered trust architecture based on client identity validation, communications history, and behavior-based reputation scoring. Conversely, the EGoT platform relies on a performance-based settlement engine ([operator.SettlementEngine](file:///home/tylor/phd/dissertation/MainMatter/methods.tex#L250-L260)) that compares scheduled actions directly against Mirror Usage Point telemetry, avoiding subjective reputation metrics.
* **Transport-Layer Security vs. Cyber-Physical Vulnerabilities:** Standard architectures rely on transport security (mTLS) as sufficient for protection. However, [sarker_cyber-physical_2020.md](file:///home/tylor/phd/notes/sarker_cyber-physical_2020.md) proves that if an attacker compromises the server-side credentials and issues malicious standard-compliant control messages (such as an incorrect Volt-VAR curve), the physical microgrid can experience voltage collapse regardless of mTLS transport security.

---

## Theme 5: Standardizing Common Grid Services and ESI Lifecycle Mappings
This theme addresses the formalization of common grid services (Energy, Reserve, Regulation, Frequency Response, Voltage Management, and Blackstart) and their integration within Energy Services Interface (ESI) lifecycles.

### Primary Sources
* [kolln_common_grid_services_energy_2023.md](file:///home/tylor/phd/notes/kolln_common_grid_services_energy_2023.md)
* [kolln_common_grid_services_reserve_2023.md](file:///home/tylor/phd/notes/kolln_common_grid_services_reserve_2023.md)
* [kolln_common_grid_services_regulation_2023.md](file:///home/tylor/phd/notes/kolln_common_grid_services_regulation_2023.md)
* [kolln_common_grid_services_frequency_response_2023.md](file:///home/tylor/phd/notes/kolln_common_grid_services_frequency_response_2023.md)
* [kolln_common_grid_services_voltage_management_2023.md](file:///home/tylor/phd/notes/kolln_common_grid_services_voltage_management_2023.md)
* [kolln_common_grid_services_blackstart_2023.md](file:///home/tylor/phd/notes/kolln_common_grid_services_blackstart_2023.md)
* [grid_services_lifecycle_review.md](file:///home/tylor/phd/notes/grid_services_lifecycle_review.md)

### Conflicting Viewpoints
* **Source-Agnostic Scheduling vs. Monolithic Device Rules:** Standard utility operations define separate rules and products based on the physical hardware type. In contrast, the GMLC report and EGoT lifecycle diagrams advocate for source-agnostic ESI mapping using generic primitives (like `sep.FlowReservationRequest`) to handle batteries, solar, and smart loads symmetrically.
* **Telemetry Adherence Verification vs. Customer Data Privacy:** To verify fast services (Regulation, Frequency Response), operators demand high-frequency (sub-second or 4-second) telemetry. However, privacy regulations and bandwidth limits restrict telemetry to hourly/daily intervals, creating a structural conflict between billing verification and privacy boundaries.
* **Blackstart Feeder Restoration vs. Demand-Side DR Load-Shedding:** Traditional utility frameworks treat residential emergency services simply as load-shedding demand response entities, whereas true blackstart restoration requires active microgrid islanding coordination, grid-forming (GFM) control, and sequential feeder synchronization.

---

# Phase 2: Project Gap Analysis

This section compares the current EGoT implementation details and future research plans against the primary literature to identify architectural and theoretical gaps.

## 1. Battery Degradation & Capacity Fading in ESS Emulators
* **Current EGoT Implementation:** In [methods.tex:L150-161](file:///home/tylor/phd/dissertation/MainMatter/methods.tex#L150-L161), the Energy Storage System (ESS) battery model is parameterized with a constant round-trip efficiency ($\eta_{chg} = \eta_{dis} = 95\%$) and operates within a static state of charge (SoC) range ($SoC_{min} \le SoC(t) \le SoC_{max}$).
* **Primary Literature Guidance:** Comprehensive energy storage reviews ([olympios_progress_2021.md](file:///home/tylor/phd/notes/olympios_progress_2021.md), [sarbu_comprehensive_2018.md](file:///home/tylor/phd/notes/sarbu_comprehensive_2018.md)) and system flexibility reviews ([kaushik_comprehensive_2022.md](file:///home/tylor/phd/notes/kaushik_comprehensive_2022.md)) show that battery efficiency is a non-linear function of power rate (C-rate) and temperature. More importantly, frequent cycling under real-time grid services (e.g., 5-minute regulation in Scenario 2.1) causes rapid physical capacity fading and degradation.
* **Identified Gap:** The EGoT ESS emulator overestimates long-term capacity availability and economic returns because it neglects degradation mechanisms. The scheduling engine lacks any penalty function for battery wear-and-tear, which would lead to sub-optimal dispatch curves in practical deployments.

## 2. Static vs. Dynamic Operating Limits and Feeder Capacity
* **Current EGoT Implementation:** The EGoT greedy scheduling engine ([methods.tex:L212-219](file:///home/tylor/phd/dissertation/MainMatter/methods.tex#L212-L219)) uses a static thermal capacity check ($C_j$) for each node to prevent overloading. Devices register their fixed capacity windows via `sep.FlowReservationRequest` resources.
* **Primary Literature Guidance:** Smart grid integration guidelines ([grid_guide_2024.md](file:///home/tylor/phd/notes/grid_guide_2024.md)) and screening technical reports ([keen_final_2022.md](file:///home/tylor/phd/notes/keen_final_2022.md)) document the utility transition toward **Dynamic Operating Limits (DOL)**. DOL calculates allowable active and reactive power limits dynamically based on real-time solar irradiance, ambient temperature, and current line loading.
* **Identified Gap:** The EGoT Flow Reservation scheduling engine is limited to static constraints. This static threshold can lead to conservative DER curtailment when lines are running cool (wasting clean generation) or fail to prevent overloads when thermal ratings drop on hot, low-wind days. The system does not implement a dynamic hosting capacity model.

## 3. Transport-Layer Security vs. Cyber-Physical Integrity
* **Current EGoT Implementation:** The security layer relies entirely on transport security via Mutual TLS (mTLS) with ECDSA P-256 curves. The client's identity (LFDI) is derived from certificate fingerprints and validated at connection time ([methods.tex:L96-106](file:///home/tylor/phd/dissertation/MainMatter/methods.tex#L96-L106)).
* **Primary Literature Guidance:** Co-simulation testbed evaluations ([sarker_cyber-physical_2020.md](file:///home/tylor/phd/notes/sarker_cyber-physical_2020.md)) prove that transport security is blind to malicious content. If the utility's upstream command system or Nginx configuration is compromised, an attacker can issue validly signed, standard-compliant `sep.DERControl` curves that force incorrect reactive support, causing immediate voltage collapse on islanded microgrids.
* **Identified Gap:** EGoT equates transport encryption with overall system security. There is no application-layer check to validate if incoming dispatch curves (Volt-VAR/Volt-Watt setpoints) lie within physically safe limits. A compromised registration registry or a rogue client could inject destabilizing controls, and the system lacks a physical verification or local fail-safe override mechanism.

## 4. Telemetry Calibration, Measurement Noise, and Topology Errors
* **Current EGoT Implementation:** The settlement engine ([methods.tex:L249-260](file:///home/tylor/phd/dissertation/MainMatter/methods.tex#L249-L260)) computes compliance accuracy ($A$) by directly comparing scheduled power against Mirror Usage Point (MUP) telemetry, assuming 100% accurate measurement transmission and a perfect OpenDSS feeder model.
* **Primary Literature Guidance:** AMI measurement credibility analyses ([lin_credibility_2019.md](file:///home/tylor/phd/notes/lin_credibility_2019.md)), voltage transformer specifications ([chen_new_2025.md](file:///home/tylor/phd/notes/chen_new_2025.md)), and smart meter error estimation models ([kong_estimation_2020.md](file:///home/tylor/phd/notes/kong_estimation_2020.md)) demonstrate that physical smart meters suffer from calibration drift, communication dropouts, and random noise. Furthermore, [luan_distribution_2013.md](file:///home/tylor/phd/notes/luan_distribution_2013.md) shows that GIS databases have a significant rate of customer-to-transformer phase mapping errors.
* **Identified Gap:** The EGoT settlement engine fails to model smart meter measurement uncertainty, which will lead to false penalties for compliant devices experiencing sensor drift or network latency. In addition, the OpenDSS simulation results assume perfect feeder topology, ignoring the reality that phase-mapping errors would corrupt Volt-VAR voltage correction profiles.

## 5. ESI Lifecycle Mappings vs. GMLC Service Definitions
* **Current EGoT Implementation:** The sequence diagrams in `egot/lifecycles/` detail the step-by-step transaction messages for the six services across Registration, Scheduling, Operation, Verification, and Settlement phases.
* **Primary Literature Guidance:** GMLC common grid service definitions (mapped in Theme 5 notes) outline the precise performance, electrical, and timing metrics required to define and verify each service.
* **Identified Gaps:**
  * **Regulation Telemetry & Settlement:** In `regulation.md`, the billing service settles regulation by checking cumulative Wh readings from `MUP`. Regulation is a sub-minute tracking service that requires high-resolution (2-second to 4-second) tracking data, the calculation of a unit-less *performance score* (precision, delay, correlation), and *power mileage* (total up/down movement).
  * **Reserve Standby & Dispatch:** In `reserve.md`, the sequence diagram lacks any contingency dispatch trigger. The verification and settlement phases fail to verify the resource's *speed of response* (spinning reserve ramp rate within 10 minutes) or monitor standby availability (state-of-charge tracking).
  * **Frequency Response Droop Verification:** In `frequency_response.md`, the ESI settles performance using cumulative Wh active energy, which is blind to transient sub-second droop responses. It fails to implement NERC-compliant droop verification (sample validation, response type classification, droop curve compliance).
  * **Voltage Management Reactive Telemetry:** In `voltage_management.md`, the client posts cumulative active energy (Wh) to `MUP`. Volt-VAR curves manage reactive power (VAR). The ESI lacks reactive power telemetry (VAR/VARh) and local voltage (V) telemetry schemas in the billing settlement phase.
  * **Blackstart Service Conceptual Alignment:** In `blackstart.md`, the sequence diagram models a standard *Demand Response (DR) load-shedding program* (sheddable capacity and load curtailment) rather than a true *blackstart restoration event* (grid-forming control activation, islanding transition, and cold-start sequential load pickup).

---

# Phase 3: Proposed Review Paper / Technical Chapter Outline

Based on the five themes mapped in Phase 1 and the architectural gaps identified in Phase 2, this section proposes a 4-section outline for a comprehensive review paper or a technical chapter in the dissertation.

## Section 1: Energy Service Interfaces (ESI) and Protocol Standardization for Common Grid Services
This section reviews the evolution of client-utility communication standards, framing the ESI as the core architectural boundary for modern distributed energy resources (DER), specifically focusing on Energy and Reserve capacity scheduling.

### Evidence to Include
* **ESI Definitions & Standard Mapping:** Contrast IEEE 2030.5, IEEE 1547.1, and OpenADR schemas for registration, discovery, and scheduling.
  * Cite: [grid_guide_2024.md](file:///home/tylor/phd/notes/grid_guide_2024.md) for ESI definition and architectural guidelines.
  * Cite: [johnson_evaluation_2021.md](file:///home/tylor/phd/notes/johnson_evaluation_2021.md) for experimental comparison of SunSpec Modbus, DNP3, and IEEE 1547.1.
  * Cite: [widergren_plug-and-play_2019.md](file:///home/tylor/phd/notes/widergren_plug-and-play_2019.md) for plug-and-play integration benefits across utilities.
* **Energy and Reserve Scheduling:** Analyze FlowReservation models for scheduling active power and reserving standby capacity, noting constraints like battery degradation.
  * Cite: [kolln_common_grid_services_energy_2023.md](file:///home/tylor/phd/notes/kolln_common_grid_services_energy_2023.md) and [kolln_common_grid_services_reserve_2023.md](file:///home/tylor/phd/notes/kolln_common_grid_services_reserve_2023.md) for service specifications.
  * Cite: [slay_adoption_2018.md](file:///home/tylor/phd/notes/slay_adoption_2018.md) for edge microcontroller constraints, and [slay_energy_2021.md](file:///home/tylor/phd/notes/slay_energy_2021.md) for ESI standard mapping.
  * Cite: [olympios_progress_2021.md](file:///home/tylor/phd/notes/olympios_progress_2021.md) for battery degradation limits on reserve schedules.

## Section 2: Active Voltage Control and Transient Grid Services Verification
This section evaluates the transition from local, static smart inverter curves to coordinated, dynamic voltage support and primary frequency response schemes, validated through quasi-static time-series (QSTS) and transient simulations.

### Evidence to Include
* **Volt-VAR & Volt-Watt Control:** Compare autonomous Volt-VAR/Volt-Watt curves with centralized optimization methods, detailing the requirement for reactive power (VAR/VARh) and voltage (V) telemetry.
  * Cite: [kolln_common_grid_services_voltage_management_2023.md](file:///home/tylor/phd/notes/kolln_common_grid_services_voltage_management_2023.md) for voltage service requirements.
  * Cite: [bello_optimal_2017.md](file:///home/tylor/phd/notes/bello_optimal_2017.md) and [iioka_appropriate_2022.md](file:///home/tylor/phd/notes/iioka_appropriate_2022.md) for autonomous secondary voltage control.
  * Cite: [dharmawardena_distributed_2022.md](file:///home/tylor/phd/notes/dharmawardena_distributed_2022.md) and [smith_analysis_2016.md](file:///home/tylor/phd/notes/smith_analysis_2016.md) for coordination methods and prevention of voltage oscillations.
* **Transient Frequency Response droop:** Analyze autonomous Frequency-Watt controls, deadband limits, and the NERC-compliant droop verification process.
  * Cite: [kolln_common_grid_services_frequency_response_2023.md](file:///home/tylor/phd/notes/kolln_common_grid_services_frequency_response_2023.md) for droop and deadband specifications.
* **Co-Simulation Frameworks & Modeling:** Detail the integration of microservice emulators with unbalanced load flow tools (OpenDSS).
  * Cite: [dugan_open_2016.md](file:///home/tylor/phd/notes/dugan_open_2016.md) for OpenDSS modeling primitives and [de_balancing_2022.md](file:///home/tylor/phd/notes/de_balancing_2022.md) for optimal power flow (OPF) complexity.
  * Cite: [deboever_impact_2020.md](file:///home/tylor/phd/notes/deboever_impact_2020.md) and [contact_application_2022.md](file:///home/tylor/phd/notes/contact_application_2022.md) for sub-15-minute time-series co-simulations.

## Section 3: High-Frequency Regulation Settlement and smart Meter Telemetry Analytics
This section examines the data-driven methods used by utilities to clean smart meter telemetry, classify customer consumption, and settle dynamic tracking services.

### Evidence to Include
* **High-Frequency Regulation Settlement:** Detail the performance score (correlation, delay, precision) and mileage calculations required for second-by-second tracking signals.
  * Cite: [kolln_common_grid_services_regulation_2023.md](file:///home/tylor/phd/notes/kolln_common_grid_services_regulation_2023.md) for regulation service metrics.
* **Clustering & Classification Techniques:** Review statistical and neural network models for customer load profiling and demand response segmentation.
  * Cite: [chang_load_2003.md](file:///home/tylor/phd/notes/chang_load_2003.md), [mutanen_customer_2011.md](file:///home/tylor/phd/notes/mutanen_customer_2011.md), and [grigoras_customer_2014.md](file:///home/tylor/phd/notes/grigoras_customer_2014.md) for classification.
  * Cite: [firoozjaei_time-series_2023.md](file:///home/tylor/phd/notes/firoozjaei_time-series_2023.md) and [wang_load_2015.md](file:///home/tylor/phd/notes/wang_load_2015.md) for deep learning (LSTM/RNN).
* **Telemetry Calibration and Errors:** Analyze algorithms that detect GIS phase errors and smart meter calibration drift.
  * Cite: [luan_distribution_2013.md](file:///home/tylor/phd/notes/luan_distribution_2013.md) for topology correction, and [lin_credibility_2019.md](file:///home/tylor/phd/notes/lin_credibility_2019.md) and [kong_estimation_2020.md](file:///home/tylor/phd/notes/kong_estimation_2020.md) for measurement credibility.

## Section 4: Security, Privacy, and Emergency Restoration (Blackstart) in Transactive Networks
This section reviews the security threat models of transactive energy platforms, detailing the trade-offs between transport security, cryptographic privacy, and emergency system restoration (Blackstart).

### Evidence to Include
* **Blackstart Restoration & Islanding:** Model true blackstart recovery, grid-forming control activation, islanding transitions, and load pickup sequences.
  * Cite: [kolln_common_grid_services_blackstart_2023.md](file:///home/tylor/phd/notes/kolln_common_grid_services_blackstart_2023.md) for blackstart restoration.
* **Cyber-Physical Vulnerabilities:** Detail security weaknesses that bypass standard transport security configurations.
  * Cite: [sarker_cyber-physical_2020.md](file:///home/tylor/phd/notes/sarker_cyber-physical_2020.md) for physical grid vulnerability to signed but malicious controls.
  * Cite: [alsaid_privacy-preserving_2022.md](file:///home/tylor/phd/notes/alsaid_privacy-preserving_2022.md) for STRIDE threat modeling.
* **Privacy Preserving Architectures:** Compare data aggregation, battery load-shaping, and cryptographic privacy mechanisms.
  * Cite: [ibrahem_privacy_2021.md](file:///home/tylor/phd/notes/ibrahem_privacy_2021.md) for homomorphic encryption and [kement_privacy_2021.md](file:///home/tylor/phd/notes/kement_privacy_2021.md) for joint real/reactive load shaping.
  * Cite: [ruddell_guidance_2020.md](file:///home/tylor/phd/notes/ruddell_guidance_2020.md) and [quinn_privacy_2009.md](file:///home/tylor/phd/notes/quinn_privacy_2009.md) for policies.
* **Trust Boundary Models:** Compare behavior-based trust metrics with direct performance verification.
  * Cite: [fernando_developing_2021.md](file:///home/tylor/phd/notes/fernando_developing_2021.md) for distributed trust vs. EGoT's direct performance-based settlement engine.
