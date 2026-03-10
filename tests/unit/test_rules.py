import os

def test_rules_file_exists():
    assert os.path.exists("openhab/conf/rules/main.rules") == True

def test_items_syntax_basic():
    with open("openhab/conf/items/home.items", "r") as f:
        content = f.read()
        assert "Group" in content or "Switch" in content