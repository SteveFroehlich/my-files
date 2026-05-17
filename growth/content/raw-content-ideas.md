# Still I rise content

add some content

---

Code should become a build artifact.

Read articles that git is broken in the AI era.

GitHub is cracking under the load, New versioning systems are coming out to address these problems. <add example>

But what if we are not realizing code is now a build artifact. It is a generated output of the new input: specs, Agents.md, skills/ etc. It belongs in artifactory or ECR not in git.

Just a thought, maybe it’s not the system, GitHub/git/version control that needs to change. It’s our mindset 🤔thoughts?

---

Business and software systems are going to start to resemble high frequency trading as AI matures here is my rationale 

AI can do more faster. So humans will move from doing the work to giving agents and software systems the rules, logic and guidance to do work on our behalf.

This transition already happened in trading (stocks, futures, options, etc) more than a decade ago. Here how it played out:

Traders use to sit in front of a web UI and do what is called point and clock trading. 

That logic moved to automated trading strategies that executed trades on the traders behalf in fractions of a second. Now milliseconds 

…expand more on human roles moving from execution to strategy…

---

The Github home feed is become SUPER useful.

I have been increasingly noticing every time I log into my personal Github, the feed on my home screen is recommending repos that are not only interesting but very useful. This feels like how social media should be.

So just sending out a reminder to folks that haven’t logged in in a while. As the AI revolution is taking off, if feels like coding is becoming more ubiquitous and Github is 100% at the center of that!

---

There are signs we are moving into the extract phase of the attract-extract cycle in AI. Specifically in ChatGPT some of the ending prompts are seeming more about keeping me in the app than providing value.

To finish the thought they want to do this if they are pursuing an ad model because add revenue is correlated with time in app. Think instagram, TikTok and facebook for existing examples.

Now is a good time to make sure you are not dependent on one LLM provider and have some familiarity with open source models. 

I am using the cycle definition from Chris Dixons book because I think it concisely captures the dynamic. For those who haven’t read read-write-own here is the definition of the cycle:

Todo.

---

The concept of friends may be dated in 2026.

I have dropped this concept in favor of bringing people into my life that help in different areas.

For example in some of the volunteer work I do I work with senior citizens who are folks I would not have shortlisted as a candidates for good friends, but we can geek out over local history and museum technology together and have a great time.

There are people I have worked with in my career I wouldn’t consider my friend but we were able to create really amazing things that have been more rewarding than many friendship’s I have had. Further these folks are someone out of the work environment I probably would not enjoy spending time with. But they are very smart and capable people and in the right environment we can create wonderful things together.

That environment being one focused on a specific outcome with preset expectations about how we will interact (eg corporate roles).

What I have thought of as traditional friends I now think of as people that help me emotionally. Eg we go out, have a good time and I come back to the rest of my life feeling rejuvenated.

Since I have made this mental switch I realized the number (and kinds) of people that can have utility in my life, and I in theirs is WAY bigger than I originally thought. 

I now interact with all kinds of folks; artists, interior designers, historians, PhD’s in quantum physics, founders/CEOs and everyone in between and it’s awesome.

---

Next post?

Helpful mental model I’m using for navigating the current AI tidal wave in tech.

there was the T model.

Then paint drip

Now your paint drip just got way wider and deeper. There is enough space there to focus on the parts that give you guide joy and energy.

AI is letting us rewrite our careers to some degree. I’m not sure how many chances like this we will get. So make it a thoughtful decision to surf the wave where you want to go.

---

Effective coding with agents:

Using right sized chunks:

AI coding becomes building a mental model of the software that will make sense and be maintainable under the model of human planned, AI executed.

Here is an example of what I have been experimenting with:
If I just stream of conciousness prompt and tell the AI what to do it doesn't define crisp atomic units of logic we can talk through together.

So what I have been doing is I think of an application and I ask for an over architecture.
Then I iterate on the architecture together until its in a state I am happy with.

Now the new part:
I have it execute the code in small logical groups that make sense to me and I can check. For example
deploy the persistence layer, S3, DB, ect
deploy the execution layer, EC2, other compute
install the app, eg create app specific tables, install the docker image, setup dirs and configs
start up the app
setup infra and logic to securely connect to the app from my device and connect

in each step I can quickly verify the logic in the code and the code did what I expect it to. Breaking it up in this way doesn't feel tedideous as checking AI output before did.

the biggest mental shift, you shouldn't move at the pace of model output/code gen. You should move at the pace of your understanding. Eg do you understand the system, do you have evals that prove your understanding is correct. Did you do some exploratory testing to double check that. I do this for each module/logical grouping before I move on to the next. It is tough to do, but ultimately you will have to do it anyway. You either do it upfront or when something breaks and the model can't fix it you do it under duress.

### debug tips

It will jump to conclusions. Make it verify what it things is wrong is actually wrong before it changes any code

cursor assumed the port was 8080, then started guessing common ones, like 3000. I had to stop it and go look up the correct one: 18789

---

Look at the history of work

- stay alive. Day by day
- Have a home
- Have work you are good at
- Have work you love

Going up maslows hierarchy 

Corporate careers aren’t associated with joy. Try to bring some joy to corporate.

Can be off putting. But I keep it authentic and don’t say tho gs I do t mean or believe. I do it for me as much as I do it for the wider org

---

The optimistic approach to AI job replacements 

If you are scared about AI taking your job, read this.

Humans are evolutionary primed to focus on the negative. It helped us survive in hunter gatherer times. It hurts us now.

Most jobs including developers will probably change due to AI. But the amount of things a single person can do will go up. Ideas will matter more, execution less as AI automates much of the execution phase.

So the good news is, yes many tasks developers now do will be automated but it also allows developers to be designers, business experts and a range of other helpful things. 

The roles of developer, designer and product manager may collapse to just builder in the future as AI allows people all those roles to do the other two.

---

Will AI automate people out of work. 

How to approach finding work in the age of AI

Zuckerberg says there will not be enough work. We need universal basic income.

This approach has a two big issues

1. It can lead to haves and have nots which leads to conflict
2. More importantly it misses the point that there are an infinite amount of problems humans have. Just look at the gap between where we are and where ppl want to be exploring the stars. More practically think about a success person who loves coffee but suffers from anxiety. They would love an energizing drink that does not trigger their anxiety like caffeine does. Solve that and you have a solid business 

So we move from mostly doers to problem finders. AI and other technology can do the work but humans need to tell it what to do and if it built the right thing. 

Points to establish 

- problems are boundless
- Problems are solvable
- Automation will continue to hep is solve problems moving us to better problems
- Maybe define what better problems mean

---

One of the most important questions when maturing an engineering organization is what does progress look like?

People want to get better but ppl need alignment on how to know if they are making progress.

Especially in particular ways

- hiring
- Ways of working
- Ect

---

Allowing for ah ha moments in your team.

Team epistemology. Have docs ppl can add to as ideas pop in their heads or as problems arise.

Have retro boards constantly available 

---

When working with AI and you ask it to do a task use the format:

“do  ‘X’, first tell me the approach you are going to take and why you believe that is the best approach, then complete X.

this way you learn as you go. There are documented studies that show negative cognitive affects of using AI (in the use case of writing, but I am assuming that applies more broadly) don’t let it happen to you.

---

Having local context matters for AI tools, and why copy paste to ChatGPT yields subpar results. here is an example from one of my projects

I was wiring up the image gitpod/openvscode-server:latest into a new project. I ran the build script and got the error message:

**#0 12.55 Reading state information...**

**#0 12.58 E: Unable to locate package apt-get**

**#0 12.58 E: Unable to locate package clean**

Looking at the Dockerfile I didn’t see the error, so I asked both ChatGPT via their web UI, which didn’t have access to the code base what possible errors could be, It did give it a code snippet around the line where apt-get was called in the dockerfile

At the same time I had cursor up and asked it the same question. While ChatGPT was thinking Cursor correctly identified the syntax error I had several lines down … missing \ and made the code change that fixed it. 

Embarrassing I couldn’t catch that, but my eyes glazed over it as there were like 15 lines of <some-package> \ and one missing didn’t jump out.

ChatGPT on the other hand thought for a few more minutes than advised me:

That error means Docker is treating a line that starts with `apt-get` as a **Dockerfile instruction** (it uppercases the first token → `APT-GET`) instead of a shell command. That happens when the line isn’t prefixed by `RUN`

Which while technically on the right track, it would have taken more steps on my part to find the missing slash and correct it.

So having the complete local context is the difference between finding and fixing an issue in seconds vs minutes. And more importantly saving my mental capacity from being wasted on fixing a syntax issue. Honestly the ideal case is the docker error is more helpful. But that is a problem less in my control to solve.

---

How improv applies to software development.

Concept of Yes and …

How rifting off of others parallels creative problem solving. 

Tag Brandon and Mel.

---

Surge sprint and lean / explore sprints 

Dev work is this constant flow that is normally suppose to get faster and more productive over time. Show graph. But this is not how humans work. Can lead to burn out. Experimenting with the concept of a surge sprint. Which is a sprint of above average delivery, meant to push the limits of the team and foster personal and system growth. You only grow when you are close to limits. 

That is followed by a lean sprint which has a below average work load and more learning and slower exploratory or reflective activities. It is meant to be a time to recover and re-energize the team.

This model more closely reflects how human physiology and psychology work.

---

Expanding on Navals description of the combinatorics of human DNA and upbringing to support of world view where every person can find a unique thing they are good at to pursue.

There is additional piece that is important to mention which is in order to do something impactful to society there has to be a comparatively large distribution of problems. 

There is something to be said for pursuing a thing for its own interest to an individual. But if you are seeking that has both personal interest/meaning and the potential to have a positive impact on society one has to focus on solving problems that matter for society. Thanks to David Deutches work we have a framework to explore this possibly and imo a theory that suggests there does exist the necessary broad diversity of problems to support each individual finding something uniquely meaningful and societally impactful problem to solve. And the wonderful idea that solving that problem will both make progress while revealing new interesting problems to pursue.

Let’s dig into how this can apply to our own life with the intent to find truly meaningful work while providing enough value to society that we can make a good living from the work.

I won’t try to claim I am a living example of this, but it is an ideal I strive for. Here are some things I have found to have utility in my life and how I am currently thinking about this topic.

---

Keep in mind the general product phases of AI

Understand the extraction phase is coming. Remember Google in the early days vs Google now (top results are all ads). Position yourself to understand the open source alternatives and what you will do when the major players (Google, open ai, Anthropic) turn their strategy from growth focus to profit. 

Note: There is some term Claude had for this ?

---

Heidi on using copilot to answer questions without needing to bring in engineers. If you are a PM in 2025 and are asking your engineers how the code works without forming your own opinion first you are being inconsiderate.

Use copilot come with an explanation, diagrams have them check for accuracy 

---

Prediction vs explanation. Need example from fabric of reality where explanation is better.

Emergent phenomena (at high levels and the refutation of reductionism. Eg 2nd law of thermodynamics)

What is a good explanation. Eg hard to vary predictions.

The reach of locally created but infinite reach.

---

How I think about context switching. 2 things

It’s like a muscle you can get better

There inherent limitations in the human brain to context switching and you have to be aware of how that works.

Can discuss some of the breadth of my context switching. Eg very technical to dealing with medical issues and loss.

---

One user ability to leave geo tagged digital objects for other. Eg in a forest preserve.

Could be physical objects like a physical puzzle or clue once solved rewards with a digital prize/object.

---

You know your engineering needs to go LLM native. But you need your business processes to be LLM native as well. Here is what I am trying 

General docs in markdown

Excel/tables all text based CSV files

Calendar and dates in text based .ics files

All in got and versioned for proper rails on the LLM changes to the docs and easy reverts.

This means your LLMs have to have access to the file system. Here are some tools for that, cursor Claude code. Copy paste works but it’s slow.

---

Software to allow a developer to get an API key and directly tie customer funds to pay that API key with a defined margin, so developers don’t take any financial responsibility/risk it organically maps to the customer demand with a clear profit margin.

---

Posted!!

AI won’t make software engineering obsolete it will make it more important. The marginal cost of creating new software is trending toward zero over time. This means the amount of software created will trend massively up. With the world running on software understanding how it works and how to manage it will be very important 

As software engineers we have to acknowledge our roles are fundamentally changing, but if you understand software you still have a very important skill. As a software engineer you are just no longer different ended in your career by knowing it. You have to find a speciizarion. Either in a technical niche AI isn’t capable in eg (something with not a lot of training data. Eg software for rockets or fpgas) or business niche like marketing or a domain like maintenance repair and operations (my current field). 

---

Performance reviews and promotions have not been enjoyable, I’m trying something new…

---

James - teaches me seller submission is usually extremely urgent. I teach him how modern security and identity models work. We both learn valuable information and the collective teams capability progresses. It’s great to have collaborative business stakeholders you can learn from and are open to learning.

---

Prediction vs explanation. How explanation has greater predictive and antipatory power. The limitations of only predictions. Eg Christmas example. Volume of people working on 12/25. 

Statistical prediction as lagging indicator.

Deutch example…

---

**Does this replicate.**

Meta. There is so much noise on the internet it’s hard to know what it true and/or valuable (even things I write) So in the interest of progress I am trying to make it easier for others to try and replicate my claims. In this way I hope everyone involved will learn something including myself.

Experiment next time there is a team member that has a lot of “opportunities” for improvement.

1. Write out the review in terms of the familiar strengths, opportunities and action plan. 
2. Then think about the outcomes that led to the belief in those particular strengths and opportunities. 
3. Rewrite the review in terms of those outcomes interleaving outcomes mapped to strengths and to opportunities. 
4. Pull out goals from those opportunities and the action plan
5. Write out specific aspirational outcomes that would bridge the gap between we’re the performance is and where manager and team members want it to be based on the goals.

Remember this applies equally to people who need performance improvements as it does to those wanting to aggressively grow their career.

Feedback. How do ppl let others know if it replicates.

Lastly this article is not generated by AI this is 100% my view based on my experience and understanding.

==========================

ChatGPT suggested improvements:

Here’s a focused, step-by-step set of improvements with the “why” for each. I’m not rewriting your article—just pinpointing changes/additions that will make it tighter, clearer, and easier to use in real reviews.

# **1) Clarify the thesis up front**

Improve: Add a one-sentence purpose at the top: “This article proposes an outcome-centric review format that reduces identity threat and keeps energy high during tough conversations.”

Why: Anchors the reader. Right now the opening jumps into the old format before stating your core claim.

# **2) Tighten terminology and keep it consistent**

Improve: Standardize capitalization and terms: “Demonstrated outcomes,” “High-level goals,” “Aspirational outcomes.” Define “outcome” precisely (observable, time-bounded, and evidenced).

Why: Consistency reduces cognitive load and prevents “outcome vs goal” confusion.

# **3) Add a simple template for each section (no rewrite—just a scaffold)**

Improve: Provide a 3-line scaffold people can copy/paste:

- Demonstrated outcome: Situation → Action → Result (+evidence link)
- High-level goal: Skill/Area → Why it matters → Timeframe
- Aspirational outcome: Success criteria → Evidence you’ll collect → Target date
Why: Managers and ICs need a repeatable pattern; STAR/SBI-style scaffolds reduce drift into trait talk.

# **4) Make “Aspirational outcomes” measurable**

Improve: Require 2–3 success criteria per aspiration (e.g., “Deliver X with p95 latency ≤ Y,” “Facilitate 3 design reviews with ≥4 peer endorsements on clarity”).

Why: Prevents vague “be better at communication.” Measurability keeps reviews actionable and promotion-ready.

# **5) Add pre-work artifacts so the meeting isn’t doing all the lifting**

Improve: Specify pre-work:

- IC fills a 1-pager listing 3–5 demonstrated outcomes with evidence links.
- Manager gathers 3–7 peer signals (short SBI blurbs).
Why: Reduces recency bias and makes the conversation about data, not memory.

# **6) Include a bias & calibration guardrail**

Improve: Add a short checklist: recency, halo/horns, attribution, and opportunity bias (“Did the business give them chances to demonstrate this?”).

Why: You already note opportunity constraints; make it an explicit guardrail so outcomes are interpreted fairly across ICs.

# **7) Separate “identity” from “behavior” using language cues**

Improve: Encourage “behavior-first” phrasing (“In meeting X, when Y happened, the response Z led to…”) and ban trait labels (“defensive person”).

Why: Aligns with your identity-threat argument and keeps feedback hearable.

# **8) Show how this maps to formal ratings (if HR requires them)**

Improve: Add a paragraph: run the outcome/goal/aspiration review first, then translate to the company rubric (leveling guide, competencies).

Why: Many orgs must produce a rating. Explaining the handoff increases adoptability.

# **9) Provide one worked micro-example (kept tiny)**

Improve: A 6–8 line example that demonstrates the template (positive and negative outcome; one goal; one aspiration with success criteria).

Why: Concrete examples reduce misinterpretation without rewriting your article.

# **10) Add follow-through mechanics**

Improve: Close with operational cadence:

- Agree on 1–2 owner-tagged aspirational outcomes.
- Create 30/60/90 check-ins with evidence links.
- Revisit/retire aspirations explicitly.
Why: Without a loop, aspirations turn into wish lists.

---

Can you beat AI community sourced. Take open source project, have AI and dev work on it independently. Have the tests be the scorer. Maybe if you build enough reputation a human can review.

---

Write up how to structure ML/DE with traditional SE team members.

- Meetings
- Ways of working

Want at least 2 of every specialty 

Roles expectations and which part of the system they handle.

---

Post about my markdown and cursor setup for ai agents.

Agents for non coders.

---

ping Google.com

Show image of good network.

Show image of bad network.

Value: with remote work we want an easy and realtime way to see if the network of a specific site is acting up. This gives that info

---

we don’t need to hire a dietitian and doctor. If we use AI + mcp (doctor site) + some quality enforcements + some payment (micro payments)

We can all have personalized diets and health care plans

---

BDD for AI for APIs / SDK

APIs expose tests in the form of BDD tests. This allows AI to know 

- all the features of the AI
    - Maybe five common useful prompts like lost all the features.
    - My task is X. Lost the relevant features of this API to complete it
- Prove the AI agents code is correct
- Integrate the social aspect

---

Most people go where they can make the most money let that guide their career path. They change their skills, interests and values to align with the company that pays the highest. 

Instead go where you are needed most that also aligns with your skills and interests. 

Example:

---

Evolution of work from hunter gatherer.

→ where we are

Future: enjoyment and happiness. Job satisfaction. Being satisfied is not enough anymore

---

---

Model context protocol description and examples 

---

llmstxt context and real use case. Contrast to persistent memory with vector databases

---

Try Cursor and give experience

---

New performance review template.

Move away from strengths and opportunities. Which get mapped to strengths and weaknesses and this wording creates associations to team members identity.

Use 

Topic. The dimension under review.

Demonstrated outcomes. Things they did or that happened. Talk about if you each outcome was “good” or could have been better (at/above/below expectations)

Growth opportunities. Both things that are bad and forward looking areas to grow into a promotion. 

---

---

Article on search GPT

https://openai.com/index/searchgpt-prototype/

---

Article on the Cursor IDE

---

## Content template

Hook-1:
i read relationship health at 50 was the best predictor of physical health at 80.
<link article>

Hook-2:

Don’t let AI rob you of a good conversation. I recently read hook1

Body:

```
Now days I do have less time for relationship building than I once did. So here is what I'm trying.

Instead of Googling / ChatGPT'ing when I want to learn something. I ask someone in my network (family, friends, colleages) the question and try to focus on making them enjoy the conversation along with me learning the concept i'm after.

I do have to put in a little work. I keep notes of who likes to talk about what. Some topics people light up about. For engineers it can be a new language updates or frameworks. For parents anything related to their kids, others are super into anything gardening.

Lastly some people reply with; you probably can just Goolge/ChatGPT that. I do two things when this happens. One I respond you're right, but the back and forth with a human is more enjoyable to me. Second I don't ask that person about that topic again.

Machines are great. People are better. I hope this helps someone, don't be afraid to have a conversation even when a machine is more efficient. Efficiency != happiness

```

---

I am making a browser extension that will allow you to chat with any site via an LLM (that supports it) instead of browse it.

DM me or comment if you want to try it out.

Here are some examples 

- eigen layer
    - markdown: https://github.com/Layr-Labs/eigenlayer-docs
    - site: https://docs.eigenlayer.xyz/eigenlayer/restaking-guides/overview
- fastHTML
    - docs html: https://docs.fastht.ml/
    - llmstxt: https://docs.fastht.ml/llms.txt
