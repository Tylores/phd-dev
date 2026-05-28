# Aggregated Water Heater System (AWHS) Optimization for Ancillary Services | Project Pillar: Methodology
**Date:** May 2026
**Status:** Peer-Reviewed Literature

## 🎯 Executive Summary
This dissertation presents a novel two-stage optimization routine to schedule an Aggregated Water Heater System (AWHS) for concurrently providing frequency regulation, frequency response, and peak demand mitigation. The algorithm models a resource recovery curve to prevent over-dispatching and opportunity costs while adjusting constraints dynamically in a sliding 24-hour window.

## 🔑 Key Arguments & Findings
* **Finding 1:** Aggregations of residential electric water heaters represent a highly flexible thermodynamic energy storage resource, but they suffer from recovery lag; if over-dispatched, their energy take is depleted, leading to long recovery times and lost market opportunities.
* **Finding 2:** A two-stage optimization algorithm using rolling forecasts (temperature, market prices, energy take) can successfully allocate reserves and dispatch capacity across multiple ancillary services (regulation, response, peak clipping) while recalculating dispatch-dependent resource recovery curves.

## 🛠️ Methodological Notes / Technical Specifications
* **Model:** Aggregated Water Heater System (AWHS) based on U.S. Census household data and hot water usage behavior patterns.
* **Algorithm:** Two-stage optimization with a rolling 24-hour look-ahead window shifting in 5-minute increments. Discrete Harmony Search (DHS) is reviewed as a potential technique.
* **Simulations:** Uses historical NOAA temperature data (2012 winter/summer) and electricity market prices (LMP). Training data: 75%-80% splits, 100-200 iterations.
* **Target Metrics:** RMSE for energy take and LMP pricing prediction is kept under 5%.

## 💡 Personal Insights & Open Questions
* **Potential Application:** The concept of dynamically recalculating a DER asset's "energy take" and recovery curves in response to dispatch commands can be integrated into the EGoT FlowReservation and DER status services. This allows the EGoT coordinator to manage physical thermal capacity constraints.
* **Gap/Next Step:** The dissertation models water heaters using census-based behavioral averages. How does individual user behavior override (e.g., manual hot water overrides, unexpected high demand) affect the aggregation reliability in real-world deployments?

## 📌 Critical Quotes
> "...present a two-stage optimization routine that schedules an Aggregated Water Heater System (AWHS) to concurrently provide three utility ancillary services, namely, frequency regulation, frequency response, and peak demand mitigation."
> "After every dispatch, the available energy take decreases and a new energy curve, the resource recovery curve, is re-calculated."
