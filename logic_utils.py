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
