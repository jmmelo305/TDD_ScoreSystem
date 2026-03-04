def add_points(game, amount):
    """Add amount × multiplier to score. Raises ValueError for invalid amounts.
    Returns game unchanged if inactive."""
    if not isinstance(amount, int) or isinstance(amount, bool) or amount <= 0:
        raise ValueError("amount must be a positive integer")
    if not game["active"]:
        return game
    game["score"] += amount * game["multiplier"]
    return game


def apply_multiplier(game, multiplier):
    """Set the game's score multiplier. Raises ValueError if multiplier < 1.
    Returns game unchanged if inactive."""
    if multiplier < 1:
        raise ValueError("multiplier must be >= 1")
    if not game["active"]:
        return game
    game["multiplier"] = multiplier
    return game


def reset_score(game):
    """Reset score to 0 and multiplier to 1. Works regardless of active status."""
    game["score"] = 0
    game["multiplier"] = 1
    return game


def is_high_score(game, threshold):
    """Return True if score is strictly greater than threshold.
    Raises ValueError if threshold < 0."""
    if threshold < 0:
        raise ValueError("threshold must be >= 0")
    return game["score"] > threshold