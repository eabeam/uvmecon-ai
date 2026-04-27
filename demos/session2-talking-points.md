# Session 2 Talking Points — UVM Faculty AI Bootcamp
**April 27, 2026 | Emily Beam**
**Format:** Watch-along demos, ~30-35 min total for Emily's portion

---

## Opening (~2 min)

- Quick recap: "Last week we covered the basics — what these tools are, chat vs. agentic AI, voice files, email drafting. Today is about workflows."
- Frame the session: "Today I'm going to show you two multi-step pipelines where AI does the mechanical parts and you check each step. The theme is: describe, propose, choose, execute, review. You stay in the driver's seat."
- Set expectations: "I'll do some of this live, and some I'll walk through with screenshots so we stay on time. Erkmen will follow with web scraping and grading automation."

---

## Demo 1: Lead in Vermont (~18-20 min)

### 1. Setup (30 sec)

- "Nick Saunders gave a talk on lead contamination that I went to, and I wanted to know: what does lead look like in Vermont? I wanted a map."
- "I downloaded TRI data from the EPA — that's the Toxics Release Inventory, it's public — filtered to Vermont and lead. A CSV. That's it."
- The point: this started from genuine curiosity, not a prepared exercise.

### 2. Live: Describe the data (~2 min)

Open Claude Code in the `lead-vt` directory. The CSV is already there.

**Type this prompt:**
```
Read vt_lead_tri.csv and give me a thorough description of what's in it.
What variables are there, what's the coverage, who are the top facilities,
and anything else I should know before analyzing it.
```

While it runs, narrate: "This is the first step in every data project — just understand what you have. I could do this by hand, but it takes 20 minutes of poking around. This takes about 30 seconds."

**React to the output naturally.** Key things to call out:
- 429 records, 36 facilities, 1987-2024
- Top 3 facilities are 85% of all releases
- The 2001 reporting threshold change (it caught this!)
- The on-site/off-site composition shift
- "It found things I wouldn't have checked immediately — like the fact that the named on-site categories don't add up to the on-site total, and it figured out why."

**Screenshot to have ready:** `01_data_description.md` (the full output) — show briefly if the live run is slow.

### 3. Live: Propose analysis ideas (~2 min)

**Type this prompt:**
```
Based on this data, propose 4 research or visualization ideas I could
pursue, ranging from a quick afternoon project to a real research project.
For each one, tell me what it would show, why it's interesting,
what additional data I'd need, and how complex it would be.
```

While it runs: "Now I'm asking it to brainstorm. This is where the human judgment matters — it's going to give me options, and I pick."

**React to the proposals.** Highlight:
- The map idea (Proposal 2 in the output) — "This is the one I want. An environmental justice map with facility locations sized by cumulative releases."
- Note: it also proposed the compositional shift chart, the natural experiment from the 2001 threshold change, and the facility life-cycles visualization. "These are all reasonable. Some are afternoon projects, some are full papers. I'm picking the map."
- **Key line:** "YOU choose what's interesting, not the AI. It generates options. You apply judgment."

**Screenshot to have ready:** `02_analysis_proposals.md` — show the summary table at the bottom if time allows.

### 4. Screenshots: Code + Map (~3 min)

Transition: "So I asked it to make the map. I'm going to show you what it produced rather than run the code live, because the Python setup takes a minute."

**Show screenshots in this order:**

1. **The Python code** (briefly, ~15 sec) — "It wrote about 60 lines of Python. I don't need to understand every line. What matters is the output."
2. **The map** (`vt_lead_map.png`) — this is the visual payoff. Linger here.

**Talk through the map:**
- "Each dot is a facility. Size is cumulative lead releases."
- "Two things jump out immediately: the Ethan Allen Firing Range in Jericho and the old GlobalFoundries plant in Essex Junction. Those two are enormous."
- "Two facilities account for 69% of all lead releases in the state."
- "The firing range is interesting — it's a National Guard site, it's been the state's single largest lead source since 2007, and it's releasing lead directly into the soil from spent ammunition. That's a completely different pollution story than the semiconductor manufacturing at GlobalFoundries."
- "This is the kind of thing where you see the map and immediately have five follow-up questions. That's the point."

### 5. Screenshots: Summary memo (~2 min)

**Show:** `03_summary_memo.md`

- "I then asked it to write a summary memo. From curiosity to data description to map to written summary — about 20 minutes of actual work."
- Highlight the key findings section: two counties contain 95% of all releases, the decline-over-time story, the limitations section
- "Notice it wrote a real limitations section — TRI is self-reported, doesn't measure actual exposure, only covers facilities above reporting thresholds. It's not perfect, but it's a reasonable first draft."
- "If I were writing a policy brief or a class exercise, I'd edit this, but the skeleton is solid."

### 6. Workflow takeaway (~2 min)

- "The point of this demo is NOT one magic prompt. It's a pipeline."
- Walk through the steps on your fingers:
  1. Describe the data
  2. Propose analysis ideas
  3. YOU choose what to pursue
  4. Generate code
  5. Review the output
  6. Write up the results
- "Each step is narrow enough to check. You're not asking the AI to 'do my research.' You're asking it to do the mechanical parts — reading 24 columns, writing boilerplate Python, drafting a first pass — and you provide the judgment at every step."
- "This is 20 minutes from download to memo. By hand, this is most of a day."

### 7. What AI was good at vs. not (~2 min)

**Good at:**
- Data orientation (reading a CSV, summarizing what's in it, catching quirks like the 2001 threshold change)
- Code generation (the map worked on the first try)
- First-draft reporting (the memo structure, limitations section)
- Proposing angles you might not think of immediately

**Not good at:**
- Knowing what's important about *Vermont specifically* — it doesn't know that Jericho is near residential areas, or what the politics of the firing range are
- Understanding the policy context — who would use this information, what decisions it could inform
- Deciding what's *worth* investigating — it proposed four ideas and they were all fine, but it can't tell you which one matters for your work
- "The AI is a very fast, very thorough research assistant who just arrived in Vermont last week. It can do anything you ask, but it doesn't know what to ask."

---

## Demo 2: BD Remote Ed (~12-15 min)

### 1. Setup (30 sec)

- "Different project, different use case. I have a paper on remote education in Bangladesh that keeps getting rejected. I used AI two ways: to clean up the code, and to stress-test the paper before resubmitting."
- "This one is about research workflow, not data exploration."

### 2. Code audit story (~4 min, screenshots)

Transition: "First, the code. This is a project I've been working on with an RA for three years."

**Show screenshot: the BEFORE folder structure**

- "51 do-files. Four subdirectories. No working master file — the last master was from June 2021, three years out of date."
- "Multiple versions of every key file: `03_vargen.do`, `03_vargen_07sep.do` — which one is current? `05_endline balance.do`, `05_endline balance_eb.do` — whose is canonical?"
- "Date-in-filename versioning. Author-in-filename versioning. 18 files in an Archive folder with no documentation."
- "Hardcoded paths everywhere — every script has `/Users/ebeam/Dropbox/...` in it. Only runs on my machine."
- "This is extremely common in economics. I'd bet most people in this room have something like this."

**Show screenshot: the AFTER repo structure**

- "8 canonical scripts. One master do-file with switches for each pipeline stage. A config template so anyone can run it. Git version control. Documentation."
- "86 old variants preserved in Archive — nothing deleted."
- Show the before/after table: "51 files to consider became 8. Zero 'which version?' questions."

**Show the $flags bug (the best one):**

- "While cleaning up, the AI found bugs. Here's my favorite."
- "There's a variable list called `$flags` — 17 missing-value indicators used as control variables in every regression. It's defined separately in 5 different scripts."
- "In 3 of those 5 scripts, one variable is wrong: `_c_child_work` instead of `_f_c_child_work`. Missing the `_f_` prefix. That means the same variable appeared twice in the regression — once as a control, once where the flag should be — and the actual missing indicator was left out."
- "This survived in 10+ archived versions across 2+ years of development. No human caught it because it's one wrong entry in a 17-item list. The AI found it by cross-referencing every `global flags` definition across all 51 files."
- "This is the kind of thing that doesn't crash. It doesn't throw an error. It just quietly makes your regressions slightly wrong."

**Time investment:** "Two Claude Code sessions — a few hours total. By hand, this is days of work, minimum. And I probably wouldn't have found the bugs."

### 3. Paper audit (~3 min, screenshots)

Transition: "Second use: adversarial review. I have a skill called `/econ-audit` that reads a paper and tries to find every methodological problem a referee would flag."

**Option A (if time allows, ~3 min):** Show the output live.
- "I'm going to run this on the paper. It takes about 60 seconds."
- While it runs: "It reads the full paper — LaTeX source, all the tables, appendix — and produces a structured audit organized by identification, statistical issues, measurement, methodology, and presentation."

**Option B (if tight on time):** Go straight to screenshots of the output.

**Show:** `econ-audit-output.md` — the summary table at the bottom is the most efficient thing to show.

Walk through 2-3 key findings:
- **A1 (Critical):** "The mediation claim — that information caused tutoring, which caused learning — is not identified. It caught this immediately."
- **B1-B3 (Critical):** "Multiple hypothesis testing. The headline learning result is below the minimum detectable effect. The heterogeneity analyses driving the inequality story are underpowered."
- **C1 (Critical):** "Differential attrition in the learning sample. It flagged this as serious and suggested Lee bounds."
- "5 critical findings, 8 important, 6 minor. In about 60 seconds."

### 4. Comparison to real referees (~3 min) — THE demo moment

Transition: "Here's the part that sold me on this. This paper has been submitted to 8 journals. I've gotten 11 referee reports and 4 editor letters with substantive comments. So I can actually check: did the AI find the same things the referees found?"

**Show:** `audit-vs-referees.md` — the Tier 1 comparison table.

**The headline:** "7 of 10 major referee concerns flagged in about 60 seconds."

Walk through the hits:
- "Attrition — every referee raised it, AI caught it. Full match."
- "MHT issues — strong match, and the AI actually added something referees didn't emphasize: the winner's curse framing."
- "Learning measure problems — good match, same concerns about the 8-item phone test."
- "Complex randomization — flagged."

Walk through the misses:
- "Short intervention duration — 4 to 8 weeks is unusually short for an education RCT. The AI has no idea. It doesn't know what's normal in the field."
- "Internal contradictions — this is the devastating one. Referees noticed that the data arm increased tutoring MORE than the information arm, but only information improved learning. If tutoring is your mechanism, that's a problem. The AI identified the identification issue abstractly but didn't run that specific falsification check against the paper's own results tables."
- "COVID fatigue — referees basically said 'we've seen too many of these papers.' The AI can't know the publication landscape."

**One more detail worth mentioning:** "The AI actually recommended *including* the conceptual model. Every referee wanted it *cut*. Sometimes it gives the opposite advice from what humans would."

### 5. Honest takeaway (~2 min)

- "It's a very good pre-submission check. Run it before you send a paper out. It catches the systematic stuff — identification problems, power issues, MHT, attrition — in a minute."
- "But it doesn't know your field. It can't run the 'wait, does this make sense given what we know about Bangladesh?' checks. It doesn't know what other papers exist. Its publication strategy advice is mediocre."
- "Think of it as: it replaces the first 80% of what a careful internal seminar discussant would say. The last 20% — the field-specific, 'have you thought about this?' insights — that's still you and your colleagues."
- "And for the code audit: it found bugs I didn't find in two years. That alone justified the time."

---

## Transition to Erkmen (~1 min)

- "Those were research workflows — data exploration and paper auditing. Erkmen is going to show you two more: getting data from the web and automating grading feedback. Same principle: AI handles the mechanical parts, you check each step."

---

## Shared Closing: What to Try First (~3-5 min, Emily + Erkmen)

After Erkmen's demos, co-present the "where to start" list. Emily covers 1-4, Erkmen covers his items.

1. **Create a voice file** (15 min, reuse forever) — "We showed this last week. Write down how you like to communicate — your tone, your defaults, what you hate. Save it. Use it every time you draft an email or a document."
2. **Run your data through the describe-propose-code pipeline** (30 min) — "Take any dataset you're working with. Ask the AI to describe it, propose ideas, generate code. You'll be surprised how fast it orients."
3. **Install /econ-audit and run it on a paper** (10 min) — "Before your next submission, run the audit. It's free. It catches the embarrassing stuff."
4. **Try inbox triage with Gmail integration** (30 min to set up) — "From last week — once it's set up, it drafts replies and sorts your email. High setup cost, but it pays off fast."

**Resources:**
- Bootcamp website (link on screen)
- skills.sh — skill library
- github.com/eabeam/econ-skills — Emily's economics-specific skills

---

## Timing Cheat Sheet

| Section | Target | Running Total |
|---|---|---|
| Opening | 2 min | 2 min |
| Lead VT: Setup | 0.5 min | 2.5 min |
| Lead VT: Live describe | 2 min | 4.5 min |
| Lead VT: Live propose | 2 min | 6.5 min |
| Lead VT: Screenshots (code + map) | 3 min | 9.5 min |
| Lead VT: Screenshots (memo) | 2 min | 11.5 min |
| Lead VT: Workflow takeaway | 2 min | 13.5 min |
| Lead VT: Good at / not good at | 2 min | 15.5 min |
| BD Remote Ed: Setup | 0.5 min | 16 min |
| BD Remote Ed: Code audit | 4 min | 20 min |
| BD Remote Ed: Paper audit | 3 min | 23 min |
| BD Remote Ed: vs. referees | 3 min | 26 min |
| BD Remote Ed: Honest takeaway | 2 min | 28 min |
| Transition to Erkmen | 1 min | 29 min |
| Shared closing (Emily's portion) | 3 min | 32 min |

**Buffer:** 3 min. If running long, cut the memo walkthrough (Demo 1, beat 5) to 30 seconds and trim the "good at / not good at" section.

---

## Backup Plans

- **If live demo breaks:** All outputs are saved as screenshots/markdown files. Switch to walkthrough mode without apology. "Let me show you what it produced when I ran this earlier."
- **If live demo is slow:** Narrate what's happening ("It's reading all 24 columns...") and transition to the saved output after 30 seconds.
- **If running long:** The BD Remote Ed code audit can compress to 2 min by showing only the before/after table and the $flags bug. The paper audit can compress by going straight to the comparison table.
- **If questions come during demos:** "Great question — hold that, we have Q&A time at the end." (Unless it's a quick clarification.)
