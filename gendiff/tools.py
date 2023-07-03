# tools.py

import json
import yaml
from itertools import chain


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
    removed = (("- " + key, data1[key]) for key in data1 if key not in data2)
    modified_old = (
        ("- " + key, data1[key])
        for key in data1
        if key in data2 and data1[key] != data2[key]
    )
    modified_new = (
        ("+ " + key, data2[key])
        for key in data1
        if key in data2 and data1[key] != data2[key]
    )
    unmodified = (
        ("  " + key, data1[key])
        for key in data1
        if key in data2 and data1[key] == data2[key]
    )
    added = (("+ " + key, data2[key]) for key in data2 if key not in data1)
    diff = dict(chain(removed, modified_old, modified_new, unmodified, added))
    return diff


def sort_diff_keys(diff):
    """
    Sort input dict by third symbol
    """
    return dict(sorted(diff.items(), key=lambda x: x[0][2]))


def format_diff(sorted_diff):
    """
    Form a string from input dict
    """
    return "\n".join([f"{key}: {value}" for key, value in sorted_diff.items()])
