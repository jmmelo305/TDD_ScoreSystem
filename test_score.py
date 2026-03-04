import pytest
from score import add_points, apply_multiplier, reset_score, is_high_score


def test_add_points_basic(game):
    assert add_points(game, 10)["score"] == 10

def test_add_points_uses_multiplier(game):
    game["multiplier"] = 3
    assert add_points(game, 5)["score"] == 15

def test_add_points_inactive(game):
    game["active"] = False
    assert add_points(game, 10)["score"] == 0

def test_add_points_invalid(game):
    with pytest.raises(ValueError):
        add_points(game, -5)
    with pytest.raises(ValueError):
        add_points(game, 0)
    with pytest.raises(ValueError):
        add_points(game, 2.5)


def test_apply_multiplier_basic(game):
    assert apply_multiplier(game, 4)["multiplier"] == 4

def test_apply_multiplier_inactive(game):
    game["active"] = False
    assert apply_multiplier(game, 5)["multiplier"] == 1

def test_apply_multiplier_invalid(game):
    with pytest.raises(ValueError):
        apply_multiplier(game, 0)


def test_reset_score(game):
    game["score"] = 100
    game["multiplier"] = 5
    result = reset_score(game)
    assert result["score"] == 0
    assert result["multiplier"] == 1

def test_reset_score_inactive(game):
    game["active"] = False
    game["score"] = 50
    assert reset_score(game)["score"] == 0


def test_is_high_score_above(game):
    game["score"] = 100
    assert is_high_score(game, 50) is True

def test_is_high_score_equal(game):
    game["score"] = 50
    assert is_high_score(game, 50) is False

def test_is_high_score_invalid(game):
    with pytest.raises(ValueError):
        is_high_score(game, -1)