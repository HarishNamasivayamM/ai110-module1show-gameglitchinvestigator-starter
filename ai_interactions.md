# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

<!-- Describe the goal you asked the agent to accomplish -->

**What did the agent do?**

<!-- List the steps the agent took (files edited, commands run, etc.) -->

**What did you have to verify or fix manually?**

<!-- Describe anything the agent got wrong or that required human review -->

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
| --- | --- | --- | --- | --- |
| Empty input `""` | Review `parse_guess()` and generate a pytest test for empty user input. | Verify that an empty string returns `False`, `None`, and `"Enter a guess."` without crashing. | Yes | Empty input is a common user action and should be handled gracefully instead of causing an exception. |
| Non-numeric input `"hello"` | Review `parse_guess()` and generate a pytest test for non-numeric text. | Verify that `"hello"` returns `False`, `None`, and `"That is not a number."` | Yes | Users may enter letters instead of numbers, so the parser should reject them cleanly. |
| Negative input `"-5"` | Review `parse_guess()` and generate a pytest test for a negative integer. | Verify that `"-5"` is safely parsed as the integer `-5` without crashing. | Yes | Negative values are outside the normal game range, but the parser should still handle the input predictably. |

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
<!-- Paste the prompt you gave the AI -->
```

**Linting output before:**

```
<!-- Paste relevant linter warnings/errors -->
```

**Changes applied:**

<!-- Describe what you changed based on the AI's suggestions -->

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->

| | Model A | Model B |
|-|---------|---------|
| **Model name** | | |
| **Response summary** | | |
| **More Pythonic?** | | |
| **Clearer explanation?** | | |

**Which did you prefer and why?**

<!-- Your conclusion -->
