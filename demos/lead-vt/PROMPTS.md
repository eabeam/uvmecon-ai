# Live Demo Prompts — Lead in Vermont

These are the exact prompts Emily types into Claude Code during the live demo. Tested and confirmed to produce good output in < 2 minutes each.

---

## Setup

Open Claude Code in the demo directory:
```bash
cd /Users/ebeam/Dropbox/Github/uvmecon-ai/demos/lead-vt
```

---

## Prompt 1: Describe the data (~90 seconds)

```
Read data/vt_lead_tri.csv. Describe what's in it:
- How many records and how many unique facilities?
- What variables are available?
- What's the time range?
- What are the top facilities by total releases?
- Any obvious data quality issues?
```

**What to expect:** It will identify 429 records, 36 facilities, 1987-2024. It will note the Ethan Allen Firing Range and GlobalFoundries as top emitters. It may flag the reporting threshold change around 2001.

**How to react:** "OK so we have 36 facilities over almost 40 years — that's enough to map. And it's already telling me something interesting — a military firing range is the biggest source."

---

## Prompt 2: Propose ideas (~90 seconds)

```
I went to a talk about lead contamination and I'm curious about
the distribution in Vermont. Given this data, propose 3-4
research or visualization ideas. For each, tell me what it would
show and what additional data I'd need.
```

**What to expect:** It will likely suggest a map, time trends, facility comparisons, and possibly an environmental justice angle. The proposals should be genuinely interesting, not generic.

**How to react:** Pick the map. "The map is the obvious first step — let's see where these facilities are." If it suggests the environmental justice angle: "That's interesting but I'd need Census data for that. Let's start with what we have."

**Key demo point:** You are choosing. The AI proposes, you decide. This is the "still needs you" moment.

---

## Fallback

If either prompt takes too long or produces weak output, switch to screenshots:
- `outputs/01_data_description.md` has the pre-generated description
- `outputs/02_analysis_proposals.md` has the pre-generated proposals

Say: "Sometimes the live demo gods aren't with us — here's what it produced when I ran this earlier."
