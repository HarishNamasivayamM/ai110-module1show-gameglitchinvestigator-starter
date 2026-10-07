from logic_utils import check_guess, update_score


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