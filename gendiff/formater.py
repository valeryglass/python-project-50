# formater.py

import itertools


def adjust_spacer(key, spaces):
    """
    Adjust lenght of spaces if key has prefix
    """
    prefixes = ["+ ", "- ", "  "]
    if any(key.startswith(prefix) for prefix in prefixes):
        return spaces[:-2]
    return spaces


def clean_keys(key):
    """
    Get keys without prefix
    """
    prefixes = ["+ ", "- ", "  "]
    if any(key.startswith(prefix) for prefix in prefixes):
        return key[2:]
    return key


def format_diff(value, replacer=" ", spaces_count=1, depth=1):
    """
    Form a string from input dict
    """
    if isinstance(value, dict):
        spaces = replacer * spaces_count * depth
        result = "{\n"
        for key, val in itertools.islice(value.items(), len(value)):
            result += (
                f"{adjust_spacer(key, spaces)}{key}: "
                f"{format_diff(val, replacer, spaces_count, depth+1)}\n"
            )
        result += f"{spaces[:-len(replacer*spaces_count)]}}}"
        return result
    else:
        return str(value)


def sort_diff(diff):
    sorted_diff = {}
    for key, value in sorted(diff.items(), key=lambda x: clean_keys(x[0])):
        if isinstance(value, dict):
            sorted_diff[key] = sort_diff(value)
        else:
            sorted_diff[key] = value
    return sorted_diff


def stylish(diff):
    sorted_diff = sort_diff(diff)
    result = format_diff(sorted_diff, " ", 4)
    return result
