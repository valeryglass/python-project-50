# test_formater.py

import pytest
from gendiff.formater import clean_keys, adjust_spacer, sort_diff, format_diff


def test_clean_keys():
    assert clean_keys("+ key") == "key"
    assert clean_keys("- key") == "key"
    assert clean_keys("  key") == "key"
    assert clean_keys("key") == "key"
    assert clean_keys("+- key") == "+- key"
    assert clean_keys("-+ key") == "-+ key"
    assert clean_keys("++ key") == "++ key"
    assert clean_keys("-- key") == "-- key"
    assert clean_keys("   key") == " key"

def test_adjust_spacer():
    assert adjust_spacer("+ key", "----") == "--"
    assert adjust_spacer("- key", "    ") == "  "
    assert adjust_spacer("  key", "....") == ".."
    assert adjust_spacer("key", "    ") == "    "
    assert adjust_spacer("+- key", "....") == "...."
    assert adjust_spacer("-+ key", "----") == "----"
    assert adjust_spacer("++ key", "----") == "----"
    assert adjust_spacer("-- key", "....") == "...."
    assert adjust_spacer("    key", "....") == ".."


def test_sort_diff():
    diff = {
        '+ key3': 'value3',
        '  key2': 'value2',
        '- key1': 'value1',
        'key4': 'value4',
        '+ prefix_key2': 'value2',
        '  prefix_key3': 'value3',
        '- prefix_key1': 'value1',
        'prefix_key4': 'value4',
        '+- key': 'value',
        '-+ key': 'value',
        '++ key': 'value',
        '-- key': 'value',
        '  key': 'value',
        '  prefix_key': 'value'
    }
    sorted_diff = sort_diff(diff)
    # Main sort case
    assert list(sorted_diff.keys()) == [
    '++ key', '+- key',
    '-+ key', '-- key',
    '  key', '- key1',
    '  key2', '+ key3',
    'key4', '  prefix_key',
    '- prefix_key1', '+ prefix_key2',
    '  prefix_key3', 'prefix_key4'
    ]

    # Empty case
    assert sort_diff({}) == {}


def test_format_diff():
    diff = {
        'key1': 'value1',
        'key2': {
            'nested1': 'value1',
            'nested2': 'value2',
        },
        'key3': {
            'nested3': {
                'nested4': 'value4',
            },
            'nested5': 'value5',
        },
    }
    expected_output = (
        "{\n"
        " key1: value1\n"
        " key2: {\n"
        "  nested1: value1\n"
        "  nested2: value2\n"
        " }\n"
        " key3: {\n"
        "  nested3: {\n"
        "   nested4: value4\n"
        "  }\n"
        "  nested5: value5\n"
        " }\n"
        "}"
    )
    # Main format case
    assert format_diff(diff) == expected_output

    # Empty case
    assert format_diff({}) == "{\n}"
