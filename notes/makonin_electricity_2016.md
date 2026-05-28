---
# Electricity, water, and natural gas consumption of a residential house in Canada from 2012 to 2014 | Project Pillar: Technical Specs
**Date:** May 2026
**Status:** Peer-Reviewed Literature

## 🎯 Executive Summary
This paper describes the Almanac of Minutely Power dataset Version 2 (AMPds2), which captures high-resolution (minutely) consumption data of electricity, water, and natural gas in a Canadian residential home over two years (730 days). It provides 11 electrical characteristics for each sub-metered circuit, along with historical climate and utility billing data, establishing a pre-cleaned benchmark for disaggregation (NILM) and energy modeling.

## 🔑 Key Arguments & Findings
* **Finding 1:** Residential energy consumption makes up a large fraction of global demand (e.g., 34% of electricity in the US), making home energy optimization vital. High-resolution sub-metering datasets are critical for training and validating algorithms for load disaggregation (NILM) and demand forecasting.
* **Finding 2:** Unlike other public datasets which leave data cleaning to individual researchers, AMPds2 is pre-cleaned to handle missing data and sensor resets, ensuring consistent and comparable benchmarking of machine learning algorithms. It provides 11 key electrical measurements, including reactive power and energy characteristics, which are often omitted.

## 🛠️ Methodological Notes / Technical Specifications
* Data collected over 730 continuous days (2012 to 2014) at a minutely sampling rate.
* Captures three resource types: Electricity (1 main meter + 19 sub-meters), Water (main meter + sub-meters), and Natural Gas (main meter).
* 11 electricity characteristics: voltage, current, frequency, displacement power factor, apparent power factor, real power, real energy, reactive power, reactive energy, apparent power, and apparent energy.
* Integrates climate data (hourly weather) and utility billing records.

## 💡 Personal Insights & Open Questions
* **Potential Application:** AMPds2 serves as a realistic residential load dataset for testing EGoT's Mirror Usage Point (MUP) logic, DER charging/discharging algorithms, and simulation modeling in OpenDSS.
* **Gap/Next Step:** The dataset represents a single house built in 1955 and renovated in 2006. How well do disaggregation (NILM) algorithms trained on AMPds2 generalize to modern homes with high penetration of behind-the-meter solar PV, smart appliances, and EVs?

## 📌 Critical Quotes
> "AMPds2 is the first dataset to capture all three main types of consumption (electricity, water, and natural gas) over a long period of time (2 years) and provide 11 measurement characteristics for electricity."
> "AMPds2 data has been pre-cleaned to provide for consistent and comparable accuracy results amongst different researchers and machine learning algorithms."
---
