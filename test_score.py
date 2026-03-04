import pytest
from score import add_points, apply_multiplier, reset_score, is_high_score


def test_add_points_basic(game):
    result = add_points(game, 10)
    assert result["score"] == 10