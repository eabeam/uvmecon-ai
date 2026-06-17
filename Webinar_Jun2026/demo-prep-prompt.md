# Live Demo — Claude Prompt

## What this is

The prompt Emily gives Claude during the live webinar demo. Start a fresh Claude session in `~/Desktop/grading-demo/`. The only thing in the folder is the Brightspace export: `downloads - economic delights/` with 3 fake student submissions.



### The assignment for students 



Before you start this assignment, **make sure you've read Chapter 10!** 

Then, answer the following questions. Your answer should total at least **350 words**

1. What market failure is caused by excessive horn honking? Can it be solved through Coase's theorem? Why or why not?
2. Then, watch [this video](https://youtu.be/tfS0oC7IkRk?si=X31EkZGo51cT7Sy9) (also below) about solving the problem of excessive horn honking in India. How do the Mumbai Police internalize the externality? 
3. Would the Mumbai Police's approach work in a city like NYC? Why or why not? 

---

## The prompt (casual version — use this one live)

I have student submissions from Brightspace in `downloads - economic delights/`. It's for "Economic Delights 4 — The Coase Theorem" in ECON 1450.

I need to grade these but I don't want the AI to ever see student names or IDs. Can you build me a pipeline that:

1. Strips out names and student IDs, saves a crosswalk somewhere I can find it later, and gives me anonymized versions to work with
2. Checks word counts — flag anything under  words
3. Grades each one against this rubric:
   - Question: "Describe the economic tradeoff illustrated by the Coase Theorem using a real-world example."
   - 0 = missing or off-topic, 1 = gets part of it, 2 = nails the tradeoff with a real example
4. Puts the real names back on at the end and gives me a CSV I can upload to Brightspace

Also, build me a guardrail so that during grading you never read PII or go outside this folder. I don't want to accidentally paste a gradebook into the conversation next time.

---

## The prompt (polished version — reference / backup)

I have a folder of student submissions downloaded from Brightspace in `downloads - economic delights/`. Each subfolder is one student's submission for "Economic Delights 4 — The Coase Theorem" in ECON 1450.

I want to build a grading pipeline that:

1. **De-identifies** the submissions — strips student names, IDs, and timestamps from the content. Writes a crosswalk mapping anonymous IDs to real names in a `pii/` folder. Writes anonymized files to `no-pii/`. The agent should never see the crosswalk or the original files after this step.

2. **Counts words** in each anonymized submission and flags any below 150 words for manual review.

3. **Grades** each anonymized submission against a rubric using Claude. The rubric is:
   - Question: "Describe the economic tradeoff illustrated by the Coase Theorem using a real-world example."
   - Score 0: Missing, off-topic, or no real-world example
   - Score 1: Identifies the tradeoff OR provides an example, but not both; or explanation is superficial
   - Score 2: Clearly identifies the tradeoff between private negotiation and regulatory intervention, uses a concrete real-world example, and connects the example back to the theorem
   - Output: JSON with anon_id, score, justification, and a review_queue flag for borderline cases

4. **Reconciles** the anonymous grades back to real student identities using the crosswalk and exports a `final_grades.csv` with student name, score, justification, and review flags.

5. **Builds a PII guardrail** — a pre-tool hook shell script that automatically blocks the agent from reading data files (`.csv`, `.xlsx`, `.dta`, etc.) directly into the conversation. Scripts can still process these files — only the agent context is restricted. It should also block Bash dump commands (`cat`, `head`, `grep`) on data files. Register it as a hook so it fires automatically on every file read.

Write the rubric as a YAML file and each pipeline step as a separate Python script. The grading script should call `claude -p` to grade each submission. Make sure the pipeline runs in order: deidentify → count_words → grade → reconcile.

**Important**: at no point should the AI agent see a student's real name, student ID, or anything that re-identifies them. The PII stays in `pii/` and never enters the conversation.

---

## Pre-demo checklist (for Emily, not for Claude)

Before going live:

- [ ] Fresh Claude session open in `~/Desktop/grading-demo/`
- [ ] Only `downloads - economic delights/` exists in the folder (no scripts, no rubric, no output)
- [ ] `fallback/` saved somewhere accessible (e.g. `~/Desktop/grading-demo-fallback/`) in case the live build stalls
- [ ] Tested the prompt at least once — Claude should produce ~6 files (rubric.yaml + 4 scripts + pii-guard hook)
- [ ] Verified the pipeline runs end-to-end after Claude builds it

---

## Fallback plan

If Claude stalls or the pipeline breaks live:

1. **Show what Claude wrote**: Even partial output is a good demo — "Here's the de-identification script it just built."
2. **Copy in pre-built scripts**: `cp ~/Desktop/grading-demo-fallback/*.py ~/Desktop/grading-demo-fallback/*.yaml .` and run them.
3. **Show pre-run output**: `~/Desktop/grading-demo-fallback/grades/final_grades.csv`

---

## Named cuts (if time is short)

1. **Skip live grading**: After Claude builds the scripts, run deidentify + count_words live, then show fallback grades: "The grading agent takes about a minute per submission. Here's what it produces."
2. **Skip live build entirely**: Show the slide with the pipeline diagram, walk through pre-built scripts, show fallback output at each stage.

---

## Reference: my actual guardrail

The demo will produce a simple version. My real one is at `~/.claude-assistant/scripts/pii-guard.sh` — 90 lines, also handles protected folders, LMS export folder-name detection, name-bearing PII zones, and per-project SAFE_PATHS unlock.

---

## Talking points (as each step runs)

1. **deidentify.py**: "This strips names, student IDs, and timestamps. It writes a crosswalk — that's the only place the real names live. The agent never sees it."

2. **count_words.py**: "First gate — if a response is under the minimum word count, it gets flagged for manual review instead of going to the agent."

3. **grade.py**: "The agent reads each anonymized response, applies the rubric, scores it 0, 1, or 2. Anything borderline gets flagged for your review."

4. **reconcile.py**: "Merges anonymous scores back to real names using the crosswalk. Exports a CSV you can upload to Brightspace."

5. **pii-guard.sh** (if demoed): "This is a guardrail I asked the agent to build. It blocks me from accidentally reading a data file into the conversation. Took about 30 seconds."
