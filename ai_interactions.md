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

```text
Review app.py, logic_utils.py, and tests/test_game_logic.py for PEP 8 style issues. Explain the pycodestyle warnings and suggest minimal formatting changes without changing the program's behavior.
```

**Linting output before:**

```text
app.py:102:10: E114 indentation is not a multiple of 4 (comment)
app.py:102:10: E116 unexpected indentation (comment)
app.py:102:80: E501 line too long (89 > 79 characters)
tests/test_game_logic.py:3:1: E302 expected 2 blank lines, found 1
tests/test_game_logic.py:37:1: E302 expected 2 blank lines, found 1
tests/test_game_logic.py:61:25: W292 no newline at end of file
```

**Changes applied:**

I corrected the indentation of the FIX comment in `app.py` and shortened the comment to stay within the PEP 8 line-length limit. I added the required blank lines between top-level test functions in `tests/test_game_logic.py` and added a newline at the end of the file. The functions in `logic_utils.py` already contained docstrings, so I reviewed them and kept them because they clearly describe each function's purpose. These formatting changes did not alter the game logic.

**Linting output after:**

```text
$ python -m pycodestyle app.py logic_utils.py tests/test_game_logic.py
No warnings or errors reported.
```

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
