# Vermont Lead Releases: TRI Data

Demo artifact for faculty AI bootcamp presentation.

## Data Provenance

- **Source**: EPA Toxics Release Inventory (TRI), via Envirofacts REST API
- **API endpoint**: `https://data.epa.gov/efservice/MV_TRI_BASIC_DOWNLOAD/ST/=/VT/CHEMICAL/CONTAINING/Lead/CSV`
- **Date downloaded**: 2026-04-24
- **Filters applied**: State = VT; Chemical contains "Lead" (captures Lead, Lead compounds, Lead And Lead Compounds)
- **Raw file**: `data/tri_raw_attempt1.csv` (122 columns, 429 rows)
- **Clean file**: `data/vt_lead_tri.csv` (24 columns, 429 rows)

## Dataset Summary

| Attribute | Value |
|---|---|
| Records | 429 |
| Unique facilities | 36 |
| Year range | 1987-2024 (38 years) |
| Counties represented | 12 |
| Chemical categories | Lead, Lead compounds, Lead And Lead Compounds |
| Units | Pounds |

## Clean CSV Columns (vt_lead_tri.csv)

| Column | Description |
|---|---|
| year | Reporting year |
| tri_facility_id | TRI facility identifier |
| facility_name | Name of reporting facility |
| street_address | Street address |
| city | City |
| county | County |
| state | State (all VT) |
| zip | ZIP code |
| latitude | Facility latitude |
| longitude | Facility longitude |
| industry_sector | Industry sector description |
| naics_code | Primary NAICS code |
| chemical | Chemical name (Lead, Lead compounds, etc.) |
| cas_number | CAS registry number |
| carcinogen | Whether classified as carcinogen (YES/NO) |
| unit_of_measure | Unit (Pounds) |
| fugitive_air_releases | Section 5.1 - Fugitive air emissions |
| stack_air_releases | Section 5.2 - Stack/point air emissions |
| water_releases | Section 5.3 - Discharges to water |
| landfill_releases | Section 5.5.1 - Landfill disposal |
| onsite_release_total | Total on-site releases |
| offsite_release_total | Total off-site releases |
| total_releases | Total releases (on-site + off-site) |
| parent_company | Parent company name |

## Top Reporting Facilities

- GE Aerospace Plant 1 (Rutland): 34 years of reports
- GE Aerospace Plant 2 (North Clarendon): 33 years
- Whitney Blake Co, Tansitor Electronics, WestRock, Simmonds Precision, Ethan Allen (2 plants): 24 years each

## Notes

- Numeric values cleaned: scientific notation zeros (e.g., `0E-10`) converted to `0`
- The TRI covers facilities that manufacture, process, or use listed chemicals above reporting thresholds; it is not a comprehensive inventory of all lead releases in Vermont
- "Lead And Lead Compounds" appears as a combined category in some years (Form A reporting)
