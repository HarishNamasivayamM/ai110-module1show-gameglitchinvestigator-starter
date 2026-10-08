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

> Compare two AI models on the same debugging task.

**Task given to both models:**

```text
Act as a Python debugging assistant.

Review this buggy guessing-game logic:

if guess > secret:
    return "Too High", "📈 Go HIGHER!"
else:
    return "Too Low", "📉 Go LOWER!"

Explain the bug and provide the simplest Pythonic fix. Do not redesign the function or add unnecessary features. Also briefly explain why your fix is correct.
```

| | Model A | Model B |
| --- | --- | --- |
| **Model name** | ChatGPT | Claude |
| **Response summary** | ChatGPT identified that the HIGHER and LOWER hint messages were reversed. It recommended keeping the existing comparison logic and swapping only the two direction messages. | Claude identified the same reversed-hint bug and recommended the same message swap. Claude also noted that equality should be handled separately if a correct guess is not already checked earlier in the function. |
| **More Pythonic?** | Yes. ChatGPT stayed focused on the smallest change needed for the existing function and did not redesign the logic. | Also Pythonic, but Claude included an additional equality-case consideration that was not necessary for this project because equality was already handled earlier in `check_guess()`. |
| **Clearer explanation?** | ChatGPT gave a concise explanation showing why each direction needed to be reversed. | Claude's explanation was slightly more detailed because it explained both comparison branches and also checked whether equality had already been handled. |

**Which did you prefer and why?**

I preferred ChatGPT's solution for this specific task because it stayed closest to the request for the simplest possible fix and matched the existing structure of the game. Both models identified the same core bug and produced the same correct HIGHER/LOWER change. Claude's explanation was slightly more thorough because it mentioned the possible equality issue, but that additional change was unnecessary in this project because `check_guess()` already checks whether the guess equals the secret before performing the higher/lower comparison.