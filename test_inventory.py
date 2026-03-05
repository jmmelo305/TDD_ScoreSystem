import pytest
from inventory import add_item, remove_item, get_item_count

def test_add_item_basic(empty_inventory):
    result = add_item(empty_inventory, "sword")
    assert "sword" in result ["items"]

def test_add_item_full_inventory(full_inventory):
    with pytest.raises(ValueError):
        add_item(full_inventory,"sword")

def test_add_item_not_string(empty_inventory):
    with pytest.raises(ValueError):
        add_item(empty_inventory, 123)

def test_add_item_empty_string_raises(empty_inventory):
    with pytest.raises(ValueError):
        add_item(empty_inventory, "")

def test_add_item_locked_returns_unchanged(locked_inventory):
    result = add_item(locked_inventory, "shield")
    assert "shield" not in result["items"]


# def test_remove_item():
    #pass

# def test_get_item_count():
    #pass

