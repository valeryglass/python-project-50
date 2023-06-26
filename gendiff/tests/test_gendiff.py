# test_gendiff.py

import pytest
import os
from gendiff.scripts.gendiff import generate_diff


@pytest.fixture
def file_path1():
    return os.path.join("gendiff", "tests", "fixtures", "file1.json")


@pytest.fixture
def file_path2():
    return os.path.join("gendiff", "tests", "fixtures", "file2.json")


@pytest.fixture
def expected_diff():
    with open(os.path.join(
                           "gendiff",
                           "tests",
                           "fixtures",
                           "expected_diff.txt"
    )) as f:
        return f.read()


def test_generate_diff(file_path1, file_path2, expected_diff):
    assert generate_diff(file_path1, file_path2) == expected_diff.strip()
