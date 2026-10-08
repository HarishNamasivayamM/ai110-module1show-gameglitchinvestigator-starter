import random


def get_range_for_difficulty(difficulty: str):
    """Return the inclusive number range for the selected difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    """Convert the user's text input into an integer guess."""
    if raw is None or raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except (ValueError, TypeError):
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess: int, secret: int):
    """Compare a guess with the secret number and return outcome and hint."""
    if guess == secret:
        return "Win", "🎉 Correct!"

    if guess > secret:
        return "Too High", "📉 Go LOWER!"

    return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update the player's score based on the guess outcome."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)

        if points < 10:
            points = 10

        return current_score + points

    if outcome in ("Too High", "Too Low"):
        return current_score - 5

    return current_score


def get_proximity_hint(guess: int, secret: int):
    """Return a user-friendly hint based on distance from the secret."""
    distance = abs(secret - guess)

    if distance <= 5:
        return "🔥 Hot! You're very close."
    if distance <= 15:
        return "🌤️ Warm! You're getting closer."

    return "❄️ Cold! You're still far away."


def update_high_score(high_score, final_score: int, won: bool):
    """Return the new high score after a game ends.

    Only winning games count. ``high_score`` is ``None`` until the
    player has won at least once this session.
    """
    if not won:
        return high_score

    if high_score is None or final_score > high_score:
        return final_score

    return high_score


def format_high_score(high_score):
    """Return a display-friendly string for the high score."""
    if high_score is None:
        return "No wins yet"

    return str(high_score)


def new_game_state(low: int, high: int, rng=random):
    """Return fresh per-game state with a secret in [low, high].

    The high score is intentionally not included so it survives
    across new games.
    """
    return {
        "secret": rng.randint(low, high),
        "attempts": 0,
        "score": 0,
        "status": "playing",
        "history": [],
    }
