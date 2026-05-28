# EGoT Literature Landscape Mapping

This document provides a landscape mapping of the literature related to the **Energy Grid of Things (EGoT)** and **Energy Service Interfaces (ESI)**, based on the notes compiled in [notes/](file:///home/tylor/phd/notes/). It outlines the four dominant themes, lists the key sources for each, and analyzes the technical and methodological conflicts between them.

---

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

*(Note: Multi-agent coordination and application deconfliction have been omitted at this time as they represent a stretch goal for grid service stacking).*
