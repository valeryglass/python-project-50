# tools.py

import json
import yaml


def generate_diff(file_path1, file_path2):
    """
    Compare two YAML/JSON files and return a string with the differences
    """
    data1 = load_data(file_path1)
    data2 = load_data(file_path2)

    diff = compare_data(data1, data2)

    return diff


def load_data(file_path):
    """
    Load data from YAML/JSON files
    """
    if file_path.endswith(".json"):
        with open(file_path) as json_file:
            return json.load(json_file)
    elif file_path.endswith(".yml") or file_path.endswith(".yaml"):
        with open(file_path) as yaml_file:
            return yaml.safe_load(yaml_file)
    else:
        raise ValueError(
            "Unsupported file format. Only JSON and YAML files are supported."
        )


def compare_data(data1, data2):
    """
    Create dict based on diff between input dicts.

    removed - keys that exist in dict1 and not exist in dict2
    modified_old - keys that exist in dict1 and exist in dict2. old value
    modified_new - keys that exist in dict1 and exist in dict2. new value
    unmodified - keys that exist in dict1 and exist in dict2. value not changed
    added - keys that exist in dict2 and not exist in dict1
    """
    diff = {}
    for key in set(data1.keys()) | set(data2.keys()):
        if key in data1 and key not in data2:
            # Key exists in dict1 but not in dict2
            diff["- " + key] = data1[key]
        elif key in data2 and key not in data1:
            # Key exists in dict2 but not in dict1
            diff["+ " + key] = data2[key]
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            # Recursively compare nested dictionaries
            nested_diff = compare_data(data1[key], data2[key])
            diff["  " + key] = nested_diff if nested_diff else None
        elif data1[key] != data2[key]:
            # Key exists in both dictionaries, but values are different
            diff["- " + key] = data1[key]
            diff["+ " + key] = data2[key]
        else:
            # Key exists in both dictionaries, and values are the same
            diff["  " + key] = data1[key]
    return diff
