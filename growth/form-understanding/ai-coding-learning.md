# AI - LLM coding and learning

AI is not a productivity tool.
It’s a force multiplier on existing discipline.

Strong teams get stronger.
Weak process gets amplified into chaos.

The job isn’t adoption — it’s containment, clarity, and compounding learning.

---

## 1. Practitioner-Led Engineering Blogs & Write-Ups (Highest Signal)

**Why this beats conferences**
- Written *after* things broke
- Shows tradeoffs, failure modes, and constraints
- Focused on code, not slides

### High-signal sources
- GitHub Engineering Blog  
  AI-assisted code review, PR workflows, guardrails, enterprise adoption
- Shopify Engineering  
  One of the clearest voices on LLMs in large-scale commerce engineering
- Stripe Engineering  
  Excellent writing on developer productivity, tooling, and safety
- Netflix Tech Blog  
  Strong on observability + AI-assisted ops patterns

**How to consume**
- Read *retroactively*: “What changed their workflow?”
- Ignore model details; focus on **integration patterns**
- Capture “rules they won’t violate”

---

## 2. Open-Source AI Dev Tooling Repos (Code > Talks)

**Why this beats conferences**
- You see *exactly* what problems people are solving
- Maintainers argue in public
- Patterns emerge before they’re named

### What to study (not endorse, just analyze)
- AI-assisted code review bots
- Agent-based developer tools
- Test generation frameworks
- Repo-level static analysis + LLM augmentation

**How to extract signal**
- Read issues labeled `bug`, `eval`, or `production`
- Look at what *didn’t* get merged
- Study config defaults — they encode lessons

---

## 3. Curated Technical Communities (Not “AI Twitter”)

**Why this beats conferences**
- Ongoing discussion
- Real constraints
- Senior engineers push back on bad ideas

### High-signal communities
- Private Slack / Discord groups focused on:
  - DevEx
  - Platform engineering
  - Internal tooling
- GitHub Discussions in serious repos
- Invite-only mailing lists run by Staff+ engineers

**What to watch for**
- Debates about *when not to use AI*
- Conversations about eval quality
- “This sounded great until prod” stories

---

## 4. Internal Experiments + Write-Your-Own RFCs (Request for Comment. IETF RFCs)
There are example of RFC from the internet standards.

**Why this beats conferences**
- You learn by *forcing clarity*
- Makes tradeoffs explicit
- Builds organizational memory

### A powerful pattern
Run a **30–60 day internal experiment**:
- AI-assisted PR reviews
- Test generation in one repo
- LLM-based CI failure triage

Then require:
- An RFC-style writeup:
  - What worked
  - What regressed
  - Where humans still dominate
  - New failure modes

This creates **compounding learning** conferences cannot.

---

## 5. Long-Form Technical Podcasts (Selective, Not Many)

**Why this beats conferences**
- Guests are less guarded
- Real stories emerge
- You hear uncertainty and evolution

### What to look for
- Episodes > 90 minutes
- Engineers describing *abandoned approaches*
- Focus on tooling, not “AI strategy”

(If a podcast avoids code entirely, skip it.)

---

## 6. Architecture Review of AI-Native Tools (Reverse Engineering)

**Why this beats conferences**
- You learn by dissecting working systems
- Forces you to reason about constraints

### How to do this
Pick 2–3 AI-native developer tools and ask:
- Where is AI used vs avoided?
- What is cached?
- What is deterministic?
- Where do humans remain in the loop?

This sharpens judgment far faster than listening to talks.

---

## The Executive Reality Check

> Conferences are **idea generators**.  
> These alternatives are **decision shapers**.

For Directors and Staff+ engineers, the winning combo is:
- **1–2 conferences per year** (for alignment)
- **Continuous exposure** to real-world artifacts like the above


