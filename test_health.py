from health import *

def test_take_damage_reduces_health():
    assert take_damage(100, 30) == 70 

def test_heal_adds_health():
    assert heal(70, 30) == 100

def test_is_alive_true():
    assert is_alive(100) == True

def test_take_damage(player):
    result = take_damage(player["health"], 30)  
    assert result == 70                          

def test_heal(injured_player):
    result = heal(injured_player["health"], 30)
    assert result == 100

def test_is_alive(dead_player):
    result = is_alive(dead_player["health"])
    assert result == False