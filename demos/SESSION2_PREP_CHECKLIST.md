# Session 2 Prep Checklist

**Sunday April 27, 11:00-12:30, Old Mill A500**
**Target: ~30 min of Emily content, then hand off to Erkmen**

---

## What's Already Done (Claude built these)

All demo artifacts exist and are ready to review. You do not need to generate anything from scratch.

**Lead in Vermont (Demo 1)**

| Artifact | Path |
|---|---|
| Live demo prompts | `/Users/ebeam/Dropbox/Github/uvmecon-ai/demos/lead-vt/PROMPTS.md` |
| TRI dataset | `/Users/ebeam/Dropbox/Github/uvmecon-ai/demos/lead-vt/data/vt_lead_tri.csv` |
| Data description (fallback) | `/Users/ebeam/Dropbox/Github/uvmecon-ai/demos/lead-vt/outputs/01_data_description.md` |
| Analysis proposals (fallback) | `/Users/ebeam/Dropbox/Github/uvmecon-ai/demos/lead-vt/outputs/02_analysis_proposals.md` |
| Summary memo | `/Users/ebeam/Dropbox/Github/uvmecon-ai/demos/lead-vt/outputs/03_summary_memo.md` |
| Map image | `/Users/ebeam/Dropbox/Github/uvmecon-ai/demos/lead-vt/outputs/vt_lead_map.png` |
| Python code | `/Users/ebeam/Dropbox/Github/uvmecon-ai/demos/lead-vt/code/make_map.py` |

**BD Remote Ed (Demo 2)**

| Artifact | Path |
|---|---|
| Before/after doc | `/Users/ebeam/Dropbox/Github/uvmecon-ai/demos/bd-remote-ed/before-after.md` |
| Bug examples | `/Users/ebeam/Dropbox/Github/uvmecon-ai/demos/bd-remote-ed/bug-examples.md` |
| Econ-audit output | `/Users/ebeam/Dropbox/Github/uvmecon-ai/demos/bd-remote-ed/outputs/econ-audit-output.md` |
| Audit vs. referees comparison | `/Users/ebeam/Dropbox/Github/uvmecon-ai/demos/bd-remote-ed/outputs/audit-vs-referees.md` |

**Session-level**

| Artifact | Path |
|---|---|
| Full talking points | `/Users/ebeam/Dropbox/Github/uvmecon-ai/demos/session2-talking-points.md` |
| Demo design spec | `/Users/ebeam/Dropbox/Github/uvmecon-ai/docs/superpowers/specs/2026-04-24-session2-demos-design.md` |
| Map in slides figures/ | `/Users/ebeam/Dropbox/Github/uvmecon-ai/Session2_Slides/figures/vt_lead_map.png` |

---

## Block 1: Read Through Everything (MUST -- 30 min)

This is the "load it into your head" pass. Don't edit yet, just read and flag anything that feels off.

- [ ] Read the talking points end to end: `/Users/ebeam/Dropbox/Github/uvmecon-ai/demos/session2-talking-points.md`
- [ ] Read the live demo prompts: `/Users/ebeam/Dropbox/Github/uvmecon-ai/demos/lead-vt/PROMPTS.md`
- [ ] Skim the before/after doc -- does it match your memory of the project? `/Users/ebeam/Dropbox/Github/uvmecon-ai/demos/bd-remote-ed/before-after.md`
- [ ] Skim the bug examples -- are you comfortable telling the `$flags` story cold? `/Users/ebeam/Dropbox/Github/uvmecon-ai/demos/bd-remote-ed/bug-examples.md`
- [ ] Read the audit-vs-referees comparison -- this is the demo's punchline: `/Users/ebeam/Dropbox/Github/uvmecon-ai/demos/bd-remote-ed/outputs/audit-vs-referees.md`
- [ ] Flag anything that needs personalizing (wrong detail, missing nuance, tone issues). Jot notes in the margins or in a scratch file.

**Done when:** You've read everything once and have a short list of edits (or you're happy with it as-is).

---

## Block 2: Test the Live Demos (MUST -- 25 min)

You are doing two things live: the data description prompt and the analysis proposals prompt. Both need to work reliably.

- [ ] Open Claude Code in the lead-vt directory: `cd /Users/ebeam/Dropbox/Github/uvmecon-ai/demos/lead-vt`
- [ ] Run Prompt 1 (data description) from `PROMPTS.md`. Time it. Should be < 90 seconds.
- [ ] Run Prompt 2 (analysis proposals) from `PROMPTS.md`. Time it. Should be < 90 seconds.
- [ ] Check: does the output naturally lead to picking the map idea? If not, adjust your reaction script.
- [ ] **DECISION: Live /econ-audit or saved output?** Run `/econ-audit` once on the paper to test it. If it runs cleanly in ~60 seconds, plan to do it live. If it's flaky or slow, plan to use the saved output at `/Users/ebeam/Dropbox/Github/uvmecon-ai/demos/bd-remote-ed/outputs/econ-audit-output.md` and walk through screenshots instead.
  - Paper location: `/Users/ebeam/Dropbox/Apps/Overleaf/Lowering Barriers to Remote Education in Bangladesh/main.tex`
- [ ] Note your decision here: Live ___ / Saved output ___

**Done when:** Both live prompts produce good output, and you've decided live vs. saved for /econ-audit.

---

## Block 3: Personalize the Talking Points (SHOULD -- 20 min)

Claude wrote the talking points. They need to sound like you.

- [ ] Go back to `/Users/ebeam/Dropbox/Github/uvmecon-ai/demos/session2-talking-points.md` and edit in place
- [ ] Add your own reactions to the Lead VT map (what jumped out when YOU first saw it?)
- [ ] Adjust the BD Remote Ed framing -- does "keeps getting rejected" feel right, or do you want softer language?
- [ ] Check the "good at / not good at" lists -- anything you want to add or cut?
- [ ] Check the "honest takeaway" section for Demo 2 -- does the 80%/20% framing match your experience?
- [ ] Review the "what to try first" list at the bottom -- is /econ-audit installable for participants? Confirm the skills.sh and github.com/eabeam/econ-skills links are live.

**Done when:** The talking points read like your voice, not Claude's.

---

## Block 4: Take Screenshots (SHOULD -- 20 min)

You need screenshots for the non-live portions. Some artifacts exist as markdown; you need actual screen captures for the slides.

**Lead VT screenshots needed:**

- [ ] The generated Python code (briefly visible): open `/Users/ebeam/Dropbox/Github/uvmecon-ai/demos/lead-vt/code/make_map.py` in an editor, screenshot
- [ ] The map: `/Users/ebeam/Dropbox/Github/uvmecon-ai/demos/lead-vt/outputs/vt_lead_map.png` (already an image -- just confirm it looks good in slides)
- [ ] The summary memo: open `03_summary_memo.md`, screenshot the key findings section

**BD Remote Ed screenshots needed:**

- [ ] The "before" folder structure: navigate to `/Users/ebeam/Dropbox/a2i project/09_Analysis&Results/02_Do files/` in Finder, screenshot showing the mess (multiple versions, date-in-filename chaos)
- [ ] The "after" repo structure: navigate to `/Users/ebeam/Dropbox/Github/bd-remote-ed/code/` in Finder, screenshot showing the clean structure
- [ ] The `$flags` bug: screenshot the relevant section from `bug-examples.md` or from the actual code diff
- [ ] The econ-audit summary table: screenshot the bottom of `/Users/ebeam/Dropbox/Github/uvmecon-ai/demos/bd-remote-ed/outputs/econ-audit-output.md`
- [ ] The audit-vs-referees Tier 1 table: screenshot from `/Users/ebeam/Dropbox/Github/uvmecon-ai/demos/bd-remote-ed/outputs/audit-vs-referees.md`

- [ ] Save all screenshots to `/Users/ebeam/Dropbox/Github/uvmecon-ai/Session2_Slides/figures/`

**Done when:** All screenshots saved in figures/ and you know which order you'll show them.

---

## Block 5: Update the Slides (SHOULD -- 30 min)

The current `s2-part1.qmd` has old Session 2 content (slide creation, teaching, CPS pipeline). It needs to be replaced with the new demo structure.

- [ ] Open `/Users/ebeam/Dropbox/Github/uvmecon-ai/slides/s2-part1.qmd`
- [ ] Replace the content to match the new demo structure (Lead VT + BD Remote Ed)
- [ ] Embed screenshots from `Session2_Slides/figures/`
- [ ] Confirm the map image renders: `Session2_Slides/figures/vt_lead_map.png`
- [ ] Add the before/after comparison table from `before-after.md` (the transformation table is great for a slide)
- [ ] Add the "7 of 10" headline and the Tier 1 comparison table from `audit-vs-referees.md`
- [ ] Add the "What to Try First" closing slide (items 1-4 from talking points)
- [ ] Render and check: does it look right?

**Done when:** Slides render cleanly with all screenshots and key tables embedded.

---

## Block 6: Erkmen Coordination (MUST -- 10 min)

- [ ] Send Erkmen the timing plan from the talking points (the table at the bottom of `session2-talking-points.md`)
- [ ] Confirm: you'll go ~30 min, he picks up at ~11:35-11:40
- [ ] Ask: does he need you to set up anything on the projector for his demos?
- [ ] Confirm: you'll co-present the "What to Try First" closing together
- [ ] Agree on who handles Q&A logistics (timer? "hold that for later"?)

**Done when:** Erkmen knows the plan and you've agreed on handoff timing.

---

## Block 7: Dry Run (NICE -- 30 min)

Talk through the whole thing out loud, alone, with a timer.

- [ ] Set a 32-minute timer
- [ ] Walk through the opening (2 min)
- [ ] Do the live demo prompts for real -- practice your narration while they run
- [ ] Walk through the screenshot portions out loud -- practice transitions
- [ ] Practice the `$flags` bug story -- can you tell it in under 60 seconds?
- [ ] Practice the "7 of 10" reveal -- this is the demo moment, make it land
- [ ] Practice the "honest takeaway" -- field norms, internal contradictions, COVID fatigue
- [ ] Check your time at the end. Over 32 min? Cut the memo walkthrough (Demo 1, beat 5) and trim "good at / not good at"

**Done when:** You've said it all out loud once and you're under 32 minutes.

---

## Day-Of Setup (MUST -- 15 min before session)

- [ ] Arrive 15 min early
- [ ] Connect to projector, test display
- [ ] Open Claude Code in `/Users/ebeam/Dropbox/Github/uvmecon-ai/demos/lead-vt/` -- ready for Prompt 1
- [ ] Open the fallback screenshots in Preview or a browser tab (data description, proposals, map, memo)
- [ ] Open the BD Remote Ed screenshots in separate tabs (before/after, bugs, audit table, comparison table)
- [ ] Open the slides deck
- [ ] Open the talking points file on your laptop screen (not projected) as a reference
- [ ] Confirm internet connection works (Claude Code needs it)
- [ ] Test font size on the projector -- can people in the back read Claude Code output?
- [ ] Have water

---

## If You're Running Out of Time (before Sunday)

**If you only have 1 hour total, do these three things:**

1. Block 1 (read everything) -- 30 min
2. Block 2 (test live demos) -- 25 min
3. Block 6 (text Erkmen the timing) -- 5 min

You can present from the talking points file alone. The markdown artifacts are your slides. Pull them up in a browser and walk through them. It won't be polished, but it will work.

**If you have 2 hours, add:**

4. Block 3 (personalize talking points) -- 20 min
5. Block 4 (screenshots) -- 20 min

**If you have 3+ hours, add:**

6. Block 5 (slides) -- 30 min
7. Block 7 (dry run) -- 30 min

**What to cut from the session itself if running long:**

- The memo walkthrough (Demo 1, beat 5) -- compress to 30 seconds: "I then asked for a summary memo. Here's the skeleton. Solid first draft, real limitations section, 20 minutes from download to written output."
- The "good at / not good at" section -- skip it, the honest takeaway in Demo 2 covers the same ground
- The before/after table details -- just show the screenshot and say "51 files became 8"

**Non-negotiable:**

- The two live prompts (this is the "wow" factor)
- The map (this is the visual payoff)
- The `$flags` bug story (this is the "AI found real bugs" proof)
- The 7-of-10 comparison (this is the punchline of the whole session)
- The honest takeaway about what AI misses (this is your credibility)

---

## Fallback Plan

If a live demo fails during the session:

> "Sometimes the live demo gods aren't with us -- here's what it produced when I ran this earlier."

Switch to the saved markdown outputs without apology. They are at:

- `/Users/ebeam/Dropbox/Github/uvmecon-ai/demos/lead-vt/outputs/01_data_description.md`
- `/Users/ebeam/Dropbox/Github/uvmecon-ai/demos/lead-vt/outputs/02_analysis_proposals.md`

If /econ-audit fails live, switch to the saved output:

- `/Users/ebeam/Dropbox/Github/uvmecon-ai/demos/bd-remote-ed/outputs/econ-audit-output.md`

Have all three open in browser tabs before you start.

---

*Last updated: 2026-04-24*
