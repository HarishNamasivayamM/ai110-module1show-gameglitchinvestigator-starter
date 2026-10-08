import random

from logic_utils import (
    check_guess,
    format_high_score,
    get_proximity_hint,
    new_game_state,
    parse_guess,
    update_high_score,
    update_score,
)


def test_winning_guess():
    """A guess equal to the secret should return a win."""
    outcome, message = check_guess(50, 50)

    assert outcome == "Win"
    assert message == "🎉 Correct!"


def test_guess_too_high():
    """A guess above the secret should tell the player to go lower."""
    outcome, message = check_guess(60, 50)

    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"


def test_guess_too_low():
    """A guess below the secret should tell the player to go higher."""
    outcome, message = check_guess(40, 50)

    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"


def test_wrong_guess_deducts_score():
    """An incorrect guess should deduct five points."""
    result = update_score(
        current_score=0,
        outcome="Too High",
        attempt_number=2,
    )

    assert result == -5


def test_empty_guess_is_rejected():
    """Empty input should be rejected without crashing."""
    ok, value, error = parse_guess("")

    assert ok is False
    assert value is None
    assert error == "Enter a guess."


def test_non_numeric_guess_is_rejected():
    """Non-numeric text should return a clear validation error."""
    ok, value, error = parse_guess("hello")

    assert ok is False
    assert value is None
    assert error == "That is not a number."


def test_negative_number_is_parsed_safely():
    """A negative integer string should be parsed without crashing."""
    ok, value, error = parse_guess("-5")

    assert ok is True
    assert value == -5
    assert error is None


def test_proximity_hints():
    """Proximity hints should reflect distance from the secret."""
    assert get_proximity_hint(48, 50) == "🔥 Hot! You're very close."
    assert get_proximity_hint(40, 50) == "🌤️ Warm! You're getting closer."
    assert get_proximity_hint(20, 50) == "❄️ Cold! You're still far away."


def test_first_win_sets_high_score():
    """The first winning score should become the high score."""
    assert update_high_score(None, 70, won=True) == 70


def test_higher_win_replaces_high_score():
    """A better winning score should replace the high score."""
    assert update_high_score(50, 80, won=True) == 80


def test_lower_win_keeps_high_score():
    """A worse winning score should not lower the high score."""
    assert update_high_score(80, 50, won=True) == 80


def test_loss_does_not_change_high_score():
    """Losing games should never affect the high score."""
    assert update_high_score(80, 500, won=False) == 80
    assert update_high_score(None, 500, won=False) is None


def test_negative_winning_score_is_recorded():
    """A win with a negative score still counts when no high score exists."""
    assert update_high_score(None, -15, won=True) == -15


def test_format_high_score():
    """High score display should handle the no-wins-yet case."""
    assert format_high_score(None) == "No wins yet"
    assert format_high_score(90) == "90"


def test_new_game_state_resets_game_and_excludes_high_score():
    """A new game resets per-game state but leaves high score alone."""
    state = new_game_state(1, 20, rng=random.Random(0))

    assert state["attempts"] == 0
    assert state["score"] == 0
    assert state["status"] == "playing"
    assert state["history"] == []
    assert "high_score" not in state


def test_new_game_secret_within_difficulty_range():
    """New game secrets should stay inside the selected range."""
    rng = random.Random(42)

    for _ in range(200):
        assert 1 <= new_game_state(1, 20, rng=rng)["secret"] <= 20
