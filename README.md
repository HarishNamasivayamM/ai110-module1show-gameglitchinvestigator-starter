# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

Game Glitch Investigator is a Streamlit number-guessing game that was intentionally provided with several logic and state bugs. The goal of the project was to reproduce the bugs, identify their causes, use AI suggestions critically, repair the game, and verify the fixes with automated and manual testing.

During testing, I found issues involving incorrect HIGHER/LOWER hints, an attempt counter that started at 1 instead of 0, inconsistent numeric comparisons, scoring that could reward an incorrect guess, and game-state problems when changing difficulty.

## 🛠️ Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the app:

```bash
python -m streamlit run app.py
```

3. Run the automated tests:

```bash
python -m pytest -v
```

## 🐛 Bugs Found

- The game started Normal difficulty with only 7 attempts remaining even though 8 attempts were allowed.
- HIGHER and LOWER hint messages were reversed.
- The secret number was converted to a string on alternating attempts, which could cause incorrect comparisons.
- Some incorrect `Too High` guesses increased the score by 5 points instead of deducting points.
- Changing difficulty could leave game state from the previous difficulty, including a secret number outside the newly displayed range.

## 🔧 Fixes Applied

- Corrected the HIGHER and LOWER hint directions in `check_guess()`.
- Kept the secret number as an integer so guesses are compared numerically.
- Changed the initial attempt count from `1` to `0`.
- Updated incorrect guesses so they consistently deduct 5 points.
- Refactored reusable game logic from `app.py` into `logic_utils.py`.
- Updated and expanded the pytest suite to verify the repaired behavior.

## 📸 Demo Walkthrough

1. The player starts a Normal game with 8 attempts available.
2. The Developer Debug Info section can be opened to inspect the secret number and current game state during testing.
3. If the secret is 50 and the player guesses 60, the game returns `Go LOWER!`.
4. If the player then guesses 40, the game returns `Go HIGHER!`.
5. Each incorrect guess deducts 5 points and uses exactly one attempt.
6. When the player enters the correct secret number, the game displays `Correct!` and ends with a final score.
7. The game logic continues to work after being refactored into `logic_utils.py`, as verified by the automated test suite.

## 🧪 Test Results

The final test suite verifies the repaired core game logic, AI-assisted edge cases, proximity hints, High Score behavior, and New Game state handling.

```text
platform win32 -- Python 3.13.12, pytest-9.1.1, pluggy-1.6.0
collected 16 items

tests/test_game_logic.py::test_winning_guess PASSED
tests/test_game_logic.py::test_guess_too_high PASSED
tests/test_game_logic.py::test_guess_too_low PASSED
tests/test_game_logic.py::test_wrong_guess_deducts_score PASSED
tests/test_game_logic.py::test_empty_guess_is_rejected PASSED
tests/test_game_logic.py::test_non_numeric_guess_is_rejected PASSED
tests/test_game_logic.py::test_negative_number_is_parsed_safely PASSED
tests/test_game_logic.py::test_proximity_hints PASSED
tests/test_game_logic.py::test_first_win_sets_high_score PASSED
tests/test_game_logic.py::test_higher_win_replaces_high_score PASSED
tests/test_game_logic.py::test_lower_win_keeps_high_score PASSED
tests/test_game_logic.py::test_loss_does_not_change_high_score PASSED
tests/test_game_logic.py::test_negative_winning_score_is_recorded PASSED
tests/test_game_logic.py::test_format_high_score PASSED
tests/test_game_logic.py::test_new_game_state_resets_game_and_excludes_high_score PASSED
tests/test_game_logic.py::test_new_game_secret_within_difficulty_range PASSED

16 passed in 0.04s
```


## 🚀 Stretch Features

### Advanced Edge-Case Testing

I used AI assistance to identify three additional input edge cases and documented the prompts and reasoning in `ai_interactions.md`.

The additional tests cover:

- Empty input `""`
- Non-numeric input `"hello"`
- Negative-number input `"-5"`

All three edge-case tests pass successfully along with the four core tests.

### Enhanced Game UI

I added proximity-based feedback to make the guessing experience more interactive. The new `get_proximity_hint()` function in `logic_utils.py` compares the player's guess with the secret number and displays one of three user-friendly hints:

- 🔥 **Hot** when the guess is within 5 numbers of the secret.
- 🌤️ **Warm** when the guess is within 15 numbers of the secret.
- ❄️ **Cold** when the guess is more than 15 numbers away.

The function is called from `app.py` after an incorrect guess, so the player now receives both the HIGHER/LOWER direction hint and a proximity hint. I manually tested all three states and confirmed that the existing game behavior continued to work.

### 🏆 High Score Tracker

The sidebar shows the best winning score achieved during the current Streamlit session (or "No wins yet" before the first win).

- Only winning games count toward the high score; losses never change it.
- Clicking **New Game** resets attempts, score, status, and guess history, and picks a new secret within the currently selected difficulty range, while keeping the high score.
- The high score lives in `st.session_state`, so it resets when the browser session ends.

The reusable logic lives in `logic_utils.py`:

- `update_high_score()` returns the new high score after a game ends.
- `format_high_score()` formats the value for display.
- `new_game_state()` builds fresh per-game state without touching the high score.

These functions are covered by additional pytest tests in `tests/test_game_logic.py`.