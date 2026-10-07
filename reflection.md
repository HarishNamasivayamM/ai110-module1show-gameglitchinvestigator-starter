# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

When I first ran the game, the Streamlit interface loaded correctly, but several parts of the game logic behaved incorrectly. I noticed that one attempt was already counted before I submitted my first guess, some higher/lower hints pointed in the wrong direction, and the score could increase even after an incorrect guess. I also noticed that changing the difficulty did not fully reset the current game state. I used the Developer Debug Info section to compare the secret number, attempts, score, and history while reproducing these problems.

### Initial Bug Reproduction Trace

```text
Normal difficulty
Range: 1 to 100
Attempts allowed: 8

Before making a guess:
Attempts left: 7
Developer Attempts: 1
Score: 0
History: []

Hint test:
Secret: 49
Guess: 50
Expected: Go LOWER!
Actual: Go HIGHER!

Scoring test:
An incorrect high guess caused the score to increase to 5.

Difficulty test:
Changed difficulty from Normal to Easy.
Easy displayed range: 1 to 20
Secret remained: 49
Previous attempts and history also remained.
```

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input / Trigger | Expected Behavior | Actual Behavior | Console Output / Error | Suspected Code Location |
| --- | --- | --- | --- | --- |
| Start a Normal game without entering a guess | The game allows 8 attempts, so it should begin with 8 attempts left and 0 attempts used | The game started with only 7 attempts left and Developer Debug Info showed Attempts = 1 | `Attempts left: 7`, `Attempts: 1`, `History: []` | `app.py`, session-state initialization for `attempts` |
| Secret = 49, enter guess = 50 | Since 50 is greater than 49, the game should tell the player to go LOWER | The game displayed `Go HIGHER!` | No exception; incorrect hint displayed | `app.py`, `check_guess()` |
| Enter an incorrect guess that is higher than the secret | A wrong guess should not increase the score | The score increased by 5 after an incorrect high guess | Developer Debug Info showed `Score: 5` | `app.py`, `update_score()` |
| Change difficulty from Normal to Easy during the game | The game state should match Easy mode and the secret should be within the displayed range of 1 to 20 | The mode changed to Easy, but the secret stayed at 49 and previous attempts/history remained | `Difficulty: Easy`, `Range: 1 to 20`, `Secret: 49` | `app.py`, difficulty and session-state handling |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

I used ChatGPT as an AI teammate while investigating and fixing the game bugs. One correct suggestion was to reverse the HIGHER and LOWER hint messages in `check_guess()`, because a guess above the secret should tell the player to go lower and a guess below it should tell the player to go higher. I verified this change using manual game testing and pytest cases for guesses above and below the secret. ChatGPT initially suggested fixing the problem by only swapping the hint messages, but I did not accept that as the complete fix because testing showed that some comparisons were still wrong when the secret was converted to a string on alternating attempts. I kept the correct hint change, revised the solution by keeping the secret as an integer for every comparison, and then verified the final version with four passing pytest tests and a live Streamlit run.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I decided a bug was fixed only after checking the behavior both manually in the Streamlit game and with automated tests. For example, after fixing the hint logic, I tested guesses above and below the secret to confirm the game returned `Go LOWER!` and `Go HIGHER!` correctly, and I also added pytest cases for those outcomes. I updated the test suite to match the refactored `check_guess()` function, which returns both an outcome and a hint message, and then ran `python -m pytest -v`. All four tests passed, including a test confirming that an incorrect guess deducts 5 points instead of increasing the score. ChatGPT helped me identify useful test cases, but I used the actual test results and live game behavior to decide whether each fix was correct.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Streamlit reruns the Python script from top to bottom whenever the user interacts with a widget, such as submitting a guess or changing a setting. Regular variables would normally be recreated during each rerun, so `st.session_state` is used to preserve values such as the secret number, score, attempts, status, and guess history between interactions. I saw this behavior while debugging because some values shown near the top of the page could reflect the state before later button-processing code updated them during that same run. This helped me understand why session state is important for keeping a Streamlit game consistent across multiple user actions.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One habit I want to reuse is reproducing a bug first, writing down the expected and actual behavior, and then making one small fix at a time instead of changing many things at once. Next time I work with AI, I would test each suggestion earlier instead of assuming that a logically correct-looking change completely solves the problem. This project showed me that AI-generated code can be useful, but it still needs careful review, testing, and human judgment before it can be trusted. I also learned that keeping clear Git commits and test evidence makes it much easier to understand what changed and verify that the program still works.