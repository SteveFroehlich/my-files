
## Experiment from prompt:
can you give me the TL Dr for this articlehttps://every.to/guides/agent-native

## content
To test these agent-native architectural claims, you should avoid heavy frameworks like LangChain. Instead, build a minimalist, local TypeScript or Python CLI prototype using the raw Anthropic or OpenAI API.

Here is a structured testing pipeline to validate the article's core hypotheses.

---

## 🏗️ 1. Setup the Shared Workspace

Validate the claim that agents thrive on a local filesystem rather than a database.

- The Directory: Create a blank local directory.
- The Context: Add a few Markdown files and JSON files representing an arbitrary user state (e.g., a simple task list or a personal journal).
- The Loop: Write a basic `while(true)` loop in code that feeds the directory structure and file contents into the LLM system prompt on every turn.

## 🛠️ 2. Build Atomic Tools (Granularity Test)

Test if tiny, primitive tools outperform complex, hardcoded workflows.

- The Code: Implement exactly 4 micro-tools exposed to the LLM:
    
    1. `read_file(path)`
    2. `write_file(path, content)`
    3. `list_directory()`
    4. `task_complete(summary)` (The explicit completion anchor)
    
- The Rule: Do not write any control flow code that chains these tools together.

## 🧪 3. Run the Emergence Test

Verify if the agent can solve unplanned, multi-step problems using only atomic tools.

- The Prompt: Give the agent a complex, ambiguous user goal.
- Example Task: _"Find all journal entries from last Tuesday, extract the action items, format them into a neat markdown table, and save it as todo.md."_
- The Evaluation: Observe the execution log. Does the agent successfully chain `list_directory` $\rightarrow$ `read_file` $\rightarrow$ `write_file` $\rightarrow$ `task_complete` without your code guiding it?

## 🔄 4. Test Feature Composability

Validate the claim that you can "ship new features" strictly by editing prompts, not code.

- The Challenge: You want to add a "Data Archiver" feature to your app.
- The Test: Do not write a single line of backend code. Instead, append a instruction to the agent's system prompt: _"When a user asks to archive, move files older than 7 days into an /archive folder."_
- The Evaluation: Ask the agent to archive your files. If it executes the task using your existing atomic tools, the composability claim is true.

## 📱 5. Simulate Mobile State Resilience

Test the mobile-specific claim regarding aggressive OS background termination.

- The Test: Trigger a multi-step task. Mid-execution (e.g., after the second tool call), forcefully kill your CLI process programmatically.
- The Evaluation: Ensure your architecture serializes the entire LLM conversation history and tool outputs to a local JSON file after _every single_ tool call. Restart the CLI. The agent should pick up exactly where it left off without repeating the first two steps.

---

If you want to start building, let me know if you would like a minimalist boilerplate code snippet for the tool-execution loop or a sample system prompt to enforce the explicit completion protocol!