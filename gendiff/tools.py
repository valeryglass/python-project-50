# tools.py

import json
import yaml
import itertools


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


# def sort_diff_keys(diff):
#     """
#     Sort input dict by third symbol
#     """
#     return dict(sorted(diff.items(), key=lambda x: x[0][2]))


def adjust_spacer(key, spaces):
    """
    Adjust lenght of spaces if key has prefix
    """
    prefixes = ["+ ", "- ", "  "]
    if any(key.startswith(prefix) for prefix in prefixes):
        return spaces[:-2]
    return spaces


def format_diff(value, replacer=" ", spaces_count=1, depth=1):
    """
    Form a string from input dict
    """
    if isinstance(value, dict):
        spaces = replacer * spaces_count * depth
        result = "{\n"
        for key, val in itertools.islice(value.items(), len(value)):
            result += f"{adjust_spacer(key, spaces)}{key}: " \
                      f"{format_diff(val, replacer, spaces_count, depth+1)}\n"
        result += f"{spaces[:-len(replacer*spaces_count)]}}}"
        return result
    else:
        return str(value)
