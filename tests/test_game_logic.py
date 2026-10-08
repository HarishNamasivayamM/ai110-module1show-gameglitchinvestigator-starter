from logic_utils import check_guess, parse_guess, update_score

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