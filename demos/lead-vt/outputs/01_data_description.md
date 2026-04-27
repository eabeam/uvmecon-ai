# Vermont Lead Releases: Data Description

**Source:** EPA Toxics Release Inventory (TRI), filtered to Vermont + lead/lead compounds
**File:** `vt_lead_tri.csv`

---

## Overview

| Dimension | Value |
|---|---|
| Records | 429 |
| Unique facilities | 36 |
| Time span | 1987--2024 (38 years, all present) |
| Unit of measure | Pounds (all records) |
| Variables | 24 columns |

---

## Variables

| Variable | Type | Description |
|---|---|---|
| `year` | Integer | Reporting year (1987--2024) |
| `tri_facility_id` | String | EPA facility identifier |
| `facility_name` | String | Facility name (36 unique) |
| `street_address` | String | Street address |
| `city` | String | City (29 unique) |
| `county` | String | County (12 unique) |
| `state` | String | Always "VT" |
| `zip` | String | ZIP code |
| `latitude` | Float | Facility latitude (42.88--45.01) |
| `longitude` | Float | Facility longitude (-73.26 to -71.51) |
| `industry_sector` | String | TRI industry classification (14 sectors) |
| `naics_code` | Integer | NAICS code |
| `chemical` | String | "Lead", "Lead compounds", or "Lead  And Lead Compounds" |
| `cas_number` | String | CAS registry number |
| `carcinogen` | String | YES/NO (232 YES, 197 NO) |
| `unit_of_measure` | String | Always "Pounds" |
| `fugitive_air_releases` | Float | Non-point air emissions (lbs) |
| `stack_air_releases` | Float | Point-source air emissions (lbs) |
| `water_releases` | Float | Direct discharges to water (lbs) |
| `landfill_releases` | Float | On-site landfill disposal (lbs) |
| `onsite_release_total` | Float | Total on-site releases (lbs) |
| `offsite_release_total` | Float | Total transferred off-site (lbs) |
| `total_releases` | Float | Grand total: onsite + offsite (lbs) |
| `parent_company` | String | Parent company (22 unique; 75 records = "NA") |

---

## Geographic Coverage

12 of Vermont's 14 counties are represented. Lamoille and Grand Isle are absent.

| County | Records | Key Facilities |
|---|---|---|
| Rutland | 86 | GE Aerospace Plants 1 & 2 |
| Chittenden | 82 | GlobalFoundries, Ethan Allen Firing Range (Jericho), Pike Industries |
| Windham | 60 | Simmonds Precision, Tansitor Electronics, Whitney Blake |
| Addison | 40 | Pike Industries (New Haven), Vergennes facilities |
| Bennington | 37 | Johnson Controls Battery Group |
| Franklin | 31 | Ethan Allen Operations (Sheldon Springs) |
| Essex | 27 | Ethan Allen Operations (Beecher Falls) |
| Orleans | 24 | Ethan Allen Operations (Orleans) |
| Caledonia | 24 | Pike Industries (Waterford) |
| Washington | 12 | Safety-Kleen, Pike Industries (Berlin) |
| Orange | 5 | Vermont Castings |
| Windsor | 1 | Ascutney Metal Products (single record) |

---

## Top Facilities by Cumulative Total Releases

| Rank | Facility | Cumulative Releases (lbs) | Years Active | Dominant Pathway |
|---|---|---|---|---|
| 1 | U.S. Army National Guard Ethan Allen Firing Range | 208,665 | 2007--2024 | On-site (ammunition) |
| 2 | GlobalFoundries U.S. 2 LLC (Essex Junction) | 152,512 | 1992--2005 | Off-site transfer |
| 3 | GE Aerospace Plant 1 (Rutland) | 82,311 | 1987--2021 | Off-site transfer (early); on-site (recent) |
| 4 | GE Aerospace Plant 2 (North Clarendon) | 37,620 | 1987--2022 | Off-site transfer |
| 5 | Johnson Controls Battery Group (Bennington) | 15,107 | 1987--1993 | Mixed air + off-site |
| 6 | Belden CDT Inc (Essex Junction) | 6,638 | 1995--2005 | Off-site/landfill |
| 7 | Champlain Cable Corp (Colchester) | 4,916 | 1993--2008 | Off-site transfer |
| 8 | U.S. Army Nat'l Guard Camp Johnson (Range) | 4,270 | 2007--2010 | On-site |
| 9 | Garware Fulflex USA (Bennington) | 2,282 | 2011--2024 | Off-site |
| 10 | Simmonds Precision Products (Vergennes) | 2,240 | 2001--2024 | Off-site |

The top 3 facilities account for **85%** of all cumulative releases. The firing range alone is 40%.

---

## Release Type Distribution

Total releases across all facilities and years: **521,410 lbs**.

### On-site vs. Off-site

| Category | Total (lbs) | Share |
|---|---|---|
| On-site releases | 228,221 | 44% |
| Off-site transfers | 293,189 | 56% |

### On-site Breakdown (named components)

| Release Type | Total (lbs) | Notes |
|---|---|---|
| Stack air | 11,011 | Point-source air emissions |
| Fugitive air | 1,567 | Non-point air emissions |
| Landfill | 1,400 | Entirely from Belden CDT (1995) |
| Water | 410 | Almost all from GlobalFoundries |

**Important note:** The four named on-site components (air, water, landfill) sum to only 14,388 lbs, but on-site total is 228,221 lbs. The gap is because TRI has additional on-site disposal categories not broken out in this extract (e.g., land treatment, surface impoundment, underground injection, on-site "other"). Most of this gap comes from the Ethan Allen Firing Range, where lead from spent ammunition is deposited on-site but does not fit neatly into air/water/landfill categories.

---

## Time Trends

### Structural break around 2001
The number of reporting facilities jumps sharply from 4 (2000) to 18 (2001). This reflects a **TRI reporting threshold change**: EPA lowered the reporting threshold for lead and lead compounds in 2001, bringing many smaller facilities into the system. Any time-series analysis must account for this.

### Three eras in the data

1. **1987--2000 (3--5 facilities):** Dominated by GE Aerospace and GlobalFoundries. Releases are almost entirely off-site transfers. Peak year is 1999 (49,121 lbs), driven by GE Aerospace Plant 1 reporting 30,265 lbs.

2. **2001--2006 (14--18 facilities):** More facilities, but total releases actually decline. GlobalFoundries stops reporting after 2005. GE declines after its 1999 spike.

3. **2007--2024 (12--18 facilities):** Dominated by the Ethan Allen Firing Range, which reports 6,700--20,300 lbs/year. The composition shifts from off-site transfers to on-site releases. 2020 was the second-highest year on record (20,589 lbs), almost entirely from the firing range.

### On-site/off-site shift
Before 2007, off-site transfers accounted for 88--100% of releases. After 2010, on-site releases dominate (85--99%), driven by the firing range. This is a meaningful compositional change: the nature of the pollution problem shifted from industrial waste transfer to direct environmental deposition.

---

## Data Quality Notes

1. **Zero-release records are common.** 101 of 429 records (24%) have total_releases = 0. These are facilities that use lead but fall below the release threshold while still meeting the manufacturing threshold. They are valid and informative (they show who handles lead even without releasing it).

2. **Parent company is often missing.** 75 records have parent_company = "NA". These tend to be smaller or independently owned facilities.

3. **Chemical naming is inconsistent.** Three variants appear: "Lead" (232), "Lead compounds" (183), and "Lead  And Lead Compounds" (14, with a double space). The distinction matters chemically (elemental lead vs. compounds like lead oxide), but for total-release analysis they can be combined.

4. **Facility names reflect current ownership.** GlobalFoundries appears back to 1992 even though IBM owned the Essex Junction fab until 2015. TRI retrospectively relabels facilities. The `tri_facility_id` field is the stable identifier.

5. **The Ethan Allen Firing Range has three separate records per year** for three different locations (Jericho, Orleans, Beecher Falls). The Jericho site dominates; the others report single-digit pounds.

6. **Onsite + offsite = total_releases** is exact for all 429 records (good internal consistency).

7. **Water releases are rare and small.** Only 26 records have any, almost all from GlobalFoundries (max 250 lbs from Johnson Controls in 1987). This is not a water-contamination dataset.
