"""Mutating functions."""

__author__ = "730664950"


def manual_append(word: list[int], number: int) -> None:
    """Print out the list."""
    word.append(number)


def double(a: list[int]) -> None:
    """Print out list after indexing."""
    idx: int = 0
    while idx < len(a):
        a[idx] *= 2
        idx += 1