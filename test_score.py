import pytest
from score import add_points, apply_multiplier, reset_score, is_high_score


def test_add_points_basic(game):
    result = add_points(game, 10)
    assert result["score"] == 10


def test_apply_multiplier_sets_value(game):
    result = apply_multiplier(game, 4)
    assert result["multiplier"] == 4


def test_reset_score_zeroes_score(game):
    game["score"] = 100
    result = reset_score(game)
    assert result["score"] == 0


def test_is_high_score_above_threshold(game):
    game["score"] = 100
    assert is_high_score(game, 50) is True