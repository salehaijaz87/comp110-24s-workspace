"""Splitting a dictionary into two lists."""

__author__ = "730664950"


def get_keys(x: dict[str, int]) -> list[str]:
    """Makes a list of all the keys in words."""
    new_list: list[str] = []
    for key in x:
        new_list.append(key)
    return (new_list)


def get_values(x: dict[str, int]) -> list[int]:
    """Make a list of all values in numbers."""
    new_list: list[int] = []
    for key in x:
        new_list.append(x[key])
    return new_list