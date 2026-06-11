# 📊 EcoRoute Telemetry Data Dictionary

The pipeline consumes simulated global multi-modal shipping manifests. Due to governance protocols, raw data arrays are kept out of version control.

### Feature Architecture Matrix
* `Distance_Miles` (Continuous): Route trajectory mileage. Injected with a 3% random missing data anomaly.
* `Payload_Tons` (Continuous): Freight volume mass transported in metric tons.
* `Traffic_Density` (Continuous): Relative delay routing coefficient tracking idling metrics. Injected with a 4% sensor dropout anomaly.
* `Dispatch_Center_ID` (High-Cardinality Categorical): Unique hub tracker designating 50+ localized operations.
* `Vehicle_Type` (Categorical): Operational fleet markers (`EV_Van`, `BioGas_Truck`, `Diesel_Rig`, `Heavy_Freight_Semi`).
* `Weather_Condition` (Categorical): Environmental parameters affecting engine drag coefficients.
* `CO2_Emissions_KG` (Target Variable): The evaluated environmental footprint output metrics.
