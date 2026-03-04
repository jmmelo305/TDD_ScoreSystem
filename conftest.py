import pytest

@pytest.fixture
def player():
    return {"health": 100, "max_health": 100, "alive": True}

@pytest.fixture
def injured_player():
    return {"health": 70, "max_health": 100, "alive": True}

@pytest.fixture
def dead_player():
    return {"health": 0, "max_health": 100, "alive": False}