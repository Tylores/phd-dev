# Impact of AMI Data Time Granularity on Quasi-Static Time-Series Load Flow Simulation | Project Pillar: Methodology
**Date:** May 2026
**Status:** Peer-Reviewed Literature

## 🎯 Executive Summary
This paper evaluates the trade-offs between data volume and simulation accuracy when utilizing Advanced Metering Infrastructure (AMI) load profiles in quasi-static time-series (QSTS) load flow simulations. By comparing 5-minute, 15-minute, and 60-minute averaged AMI data against a high-resolution 1-minute baseline using OpenDSS, the authors demonstrate that while hourly data is sufficient for general primary feeder modeling, sub-15-minute (preferably 5-minute) granularity is required to capture localized low-voltage violations and peak thermal loadings.

## 🔑 Key Arguments & Findings
* **Finding 1:** Coarser time granularities (especially 60-minute data) fail to capture the transient peaks and troughs of load demand, leading to significant underestimation of peak thermal loadings and minimum node voltages in secondary circuits.
* **Finding 2:** 15-minute data granularity is sufficient to capture primary (medium-voltage) feeder dynamics, but 5-minute granularity represents the optimal compromise for low-voltage secondary systems, capturing localized extreme events while requiring only 1/5th of the data volume and processing overhead of a 1-minute simulation.

## 🛠️ Methodological Notes / Technical Specifications
* **Simulation Engine:** EPRI "Ckt5" distribution feeder model (12.47 kV, 5 km length, 1,379 residential loads, 591 service transformers) simulated in OpenDSS via a Python COM interface.
* **Data Sources:** 1-minute resolution active power profiles from Pecan Street Inc. with synthetic randomized reactive power factors (between 0.79 and 0.99, updated every 30 minutes).
* **Data Management:** High-performance Hierarchical Data Format (HDF) files used to manage 5.4 GB input and 13.5 GB output datasets (~1.45 billion simulation data points).
* **Granularities Evaluated:** 1-minute (reference), 5-minute, 15-minute, and 60-minute (hourly).

## 💡 Personal Insights & Open Questions
* **Potential Application:** Directly impacts EGoT's Mirror Usage Point (MUP) and simulation environments. It indicates that the telemetry export tool (`data-export`) must handle sub-15-minute (ideally 5-minute) intervals to reliably identify localized grid violations in OpenDSS. It also justifies using HDF5 over flat CSV files for managing simulation telemetry.
* **Gap/Next Step:** The study assumes perfect, uninterrupted AMI data collection. Investigating how data dropouts, transmission latency, or packet losses affect QSTS accuracy at different granularities would be a highly valuable next step.

## 📌 Critical Quotes
> "...while lower time granularities of AMI data may capture feeder operation in general at the medium-voltage level, AMI data with high granularity is necessary to accurately capture feeder maximum element loadings and minimum node voltages..."
> "...with 5-minute time granularity, the feeder minimum node voltages and maximum element thermal loadings were fairly well captured at both medium-voltage and low-voltage level."
