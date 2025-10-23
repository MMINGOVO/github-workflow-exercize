import sys
import os

# 定义目标目录的绝对路径
target_dir = r"C:\Users\12189\Desktop\example_1"

# 将目录添加到 Python 搜索的路径
if target_dir not in sys.path:
    sys.path.append(target_dir)

from app.app import dedupe_header

def test_unique_columns():
    assert dedupe_header(["id", "name", "age"]) == ["id", "name", "age"]

def test_duplicate_columns():
    assert dedupe_header(["id", "id", "id"]) == ["id", "id.1", "id.2"]

def test_mixed_columns():
    cols = ["id", "name", "id", "name", "name"]
    expected = ["id", "name", "id.1", "name.1", "name.2"]
    assert dedupe_header(cols) == expected