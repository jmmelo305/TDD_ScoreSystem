import pytest
from inventory import add_item, remove_item, get_item_count


def test_add_item_basic(empty_inventory):
    result = add_item(empty_inventory, "sword")
    assert "sword" in result["items"]


def test_add_item_full_inventory(full_inventory):
    with pytest.raises(ValueError):
        add_item(full_inventory, "sword")


def test_add_item_not_string(empty_inventory):
    with pytest.raises(ValueError):
        add_item(empty_inventory, 123)


def test_add_item_empty_string_raises(empty_inventory):
    with pytest.raises(ValueError):
        add_item(empty_inventory, "")


def test_remove_item_basic(empty_inventory):
    empty_inventory["items"].append("sword")
    result = remove_item(empty_inventory, "sword")
    assert "sword" not in result["items"]


def test_remove_item_not_found_raises(empty_inventory):
    with pytest.raises(ValueError):
        remove_item(empty_inventory, "sword")


def test_remove_item_locked_returns_unchanged(locked_inventory):
    result = remove_item(locked_inventory, "sword")
    assert "sword" in result["items"]


def test_get_item_count_empty(empty_inventory):
    assert get_item_count(empty_inventory) == 0


def test_get_item_count_locked(locked_inventory):
    assert get_item_count(locked_inventory) == 1
