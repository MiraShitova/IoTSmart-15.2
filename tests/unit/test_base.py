import os

def test_files_existence():
    assert os.path.exists("conf/items/base.items")
    assert os.path.exists("conf/rules/base.rules")

def test_item_classes():
    with open("conf/items/base.items", "r") as f:
        content = f.read()
        assert "Group" in content
        assert "Switch" in content

def test_rule_logic():
    with open("conf/rules/base.rules", "r") as f:
        content = f.read()
        assert "rule" in content
        assert "when" in content