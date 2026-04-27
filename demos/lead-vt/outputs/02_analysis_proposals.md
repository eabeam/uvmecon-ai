# Vermont Lead Releases: Analysis Proposals

Four research/visualization ideas, ordered roughly from quick-win to deeper investigation.

---

## 1. The Compositional Shift: Who's Polluting Now vs. Then?

**What it would show:** An animated or faceted time-series that decomposes total Vermont lead releases by facility (or facility type), making visible the dramatic handoff from *industrial off-site transfers* (GE Aerospace, GlobalFoundries) to *military on-site deposition* (Ethan Allen Firing Range). The story isn't just "releases went down" -- it's that the *nature* of the pollution changed completely.

**Why it's interesting:** The standard TRI story is "regulation works, releases decline." Vermont's lead data complicates that. Total releases in 2020 (20,589 lbs) were higher than in 1993 (7,969 lbs). But the mix is entirely different: 1990s releases were semiconductor waste shipped to treatment facilities; 2020 releases are spent ammunition deposited directly into soil at a National Guard range in Jericho. These have completely different environmental and health implications. A stacked area chart by facility, with annotations at key transitions (GlobalFoundries exits 2005, firing range enters 2007), tells a genuinely surprising story.

**Additional data needed:** None -- this is fully doable with the existing CSV.

**Complexity:** Quick afternoon project. A stacked area chart in Python (matplotlib or plotly) or R (ggplot2) with 3--4 facility groups and a few annotations.

---

## 2. Lead and Proximity: Environmental Justice in Rural Vermont

**What it would show:** A map of Vermont's 36 TRI lead facilities, sized by cumulative releases, overlaid with demographic data -- income, race/ethnicity, housing age, and childhood blood lead level data if available. The environmental justice literature overwhelmingly focuses on urban settings. Vermont offers a test of whether the same patterns hold in a rural, predominantly white state where the variation is more about income and housing stock than race.

**Why it's interesting:** Three angles make this compelling for a Vermont economist:

- **The Rutland corridor.** GE Aerospace's two plants (Rutland + North Clarendon) released 120,000+ lbs of lead over 35 years in a county that has experienced significant economic decline. Did the plants' operational changes track with local economic shifts?
- **The Essex Junction cluster.** GlobalFoundries (formerly IBM) and Belden CDT are within a few miles of each other in Vermont's most prosperous county. How does lead exposure from high-tech manufacturing distribute across neighborhoods?
- **Military facilities as polluters.** The Ethan Allen Firing Range in Jericho is the state's largest lead source. Military installations are often exempt from local zoning and environmental review. Who lives nearby?

**Additional data needed:**
- Census tract demographics (American Community Survey -- free, via `tidycensus` or `cenpy`)
- Vermont childhood blood lead level data (VT Dept of Health publishes town-level data)
- School locations (NCES -- free)
- Housing vintage data (ACS)

**Complexity:** Multi-week project. The mapping is straightforward; the interesting part is the statistical analysis of proximity and demographics. Could be a solid undergraduate thesis or a short empirical note.

---

## 3. The 2001 Reporting Threshold Change as a Natural Experiment

**What it would show:** An analysis of what the 2001 TRI reporting threshold reduction *revealed* about lead use in Vermont. Before 2001, only 3--5 facilities reported. After 2001, 14--18 did. The newly-visible facilities (Simmonds Precision, Tansitor Electronics, Whitney Blake, Ethan Allen furniture, WestRock paper, etc.) were using lead all along but fell below the old threshold.

**Why it's interesting:** This is a clean example of how **regulation creates data, not just compliance.** An economist could use this to estimate:

- How much lead handling was invisible under the old threshold? (Answer: quite a bit -- at least a dozen facilities.)
- Did the reporting requirement itself change behavior? The literature on "disclosure effects" suggests that simply requiring public reporting reduces pollution, independent of any emissions cap. You could test this with a difference-in-differences design: facilities that were already reporting (GE, GlobalFoundries) vs. facilities that started reporting in 2001.
- What does the composition of newly-reporting facilities tell us about Vermont's industrial base? Furniture (Ethan Allen), paper (WestRock), defense electronics (Simmonds, Tansitor) -- these are not the industries people typically associate with lead.

**Additional data needed:**
- National TRI data for a comparison group (other small states, or New England)
- Facility-level production or employment data to control for scale (County Business Patterns or BLS QCEW)
- Possibly the TRI Form R filings themselves for the "production ratio" field

**Complexity:** This is a real research project -- multi-week at minimum. But the identification strategy is clean, the data is public, and the policy relevance is immediate (EPA periodically revisits TRI thresholds). Could anchor a research paper or a compelling policy brief.

---

## 4. Facility Life Cycles: Entry, Exit, and What Happens to the Lead

**What it would show:** A timeline visualization of every facility's reporting life -- when they entered the TRI, when they exited, and what their release trajectory looked like. Think of a Gantt-chart-style display with release magnitude encoded as bar thickness or color, annotated with known corporate events (GE divesting, GlobalFoundries acquisition, plant closures).

**Why it's interesting:** Several facility stories jump out from the data:

- **GE Aerospace Plant 1** had a wild spike to 30,265 lbs in 1999 (6x its usual level), then declined to near-zero by 2021. What happened in 1999? Likely a one-time cleanup or process change that generated a large off-site transfer. But from the data alone, it looks alarming.
- **GlobalFoundries** (formerly IBM) went from the state's largest lead source to *not reporting at all* after 2005. Did they eliminate lead from their process, or did they restructure reporting?
- **Johnson Controls Battery Group** reported for only 7 years (1987--1993) then disappears. Did the facility close, or did they shift below the reporting threshold?
- **Pike Industries** (asphalt/aggregates) has four separate Vermont facilities reporting since 2009, all with zero releases most years. They handle lead-containing materials but release essentially nothing -- a story about modern containment practices.

This is essentially a data journalism piece: using the administrative record to reconstruct industrial history.

**Additional data needed:**
- Local newspaper archives or VT DEC records for context on specific events
- SEC filings or press releases for major corporate transitions
- TRI Form R "source reduction" fields (available from EPA but not in this extract)

**Complexity:** The visualization itself is a solid afternoon. The research behind the annotations could take a few days of digging. The result would be an excellent teaching tool or public-facing data story.

---

## Summary Table

| Proposal | Core Question | Extra Data? | Complexity |
|---|---|---|---|
| 1. Compositional shift | Has pollution actually declined, or just changed form? | No | Afternoon |
| 2. Environmental justice | Who lives near Vermont's lead sources? | Census, health data | Multi-week |
| 3. Threshold natural experiment | Does disclosure itself reduce pollution? | National TRI, employment | Research project |
| 4. Facility life cycles | What corporate stories hide in the admin data? | News, SEC filings | Days |
