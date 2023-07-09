# # test_tools.py

# import pytest
# import os
# from gendiff.tools import generate_diff


# @pytest.fixture
# def file_path1():
#     return os.path.join("gendiff", "tests", "fixtures", "file12.json")


# @pytest.fixture
# def file_path2():
#     return os.path.join("gendiff", "tests", "fixtures", "file22.json")


# @pytest.fixture
# def expected_diff():
#     with open(os.path.join(
#                            "gendiff",
#                            "tests",
#                            "fixtures",
#                            "expected_diff02.txt"
#     )) as f:
#         return f.read()


# def test_generate_diff(file_path1, file_path2, expected_diff):
#     assert generate_diff(file_path1, file_path2) == expected_diff.strip()
