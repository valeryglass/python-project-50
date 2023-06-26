# test_gendiff.py

import pytest
from gendiff.scripts.gendiff import generate_diff


@pytest.fixture
def file_path1():
    return 'file1.json'


@pytest.fixture
def file_path2():
    return 'file2.json'


def test_generate_diff(file_path1, file_path2):
    expected_diff = """{
- follow: False
  host: hexlet.io
- proxy: 123.234.53.22
- timeout: 50
+ timeout: 20
+ verbose: True
}"""
    assert generate_diff(file_path1, file_path2) == expected_diff
