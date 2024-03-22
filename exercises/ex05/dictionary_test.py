"""Testing my functions from dictionary."""

__author__:"730664950"

from exercises.ex05.dictionary import invert
from exercises.ex05.dictionary import favorite_color
from exercises.ex05.dictionary import count
from exercises.ex05.dictionary import alphabetizer
from exercises.ex05.dictionary import update_attendance

def test_invert_short() -> None:
    """Invert a short dictionary of items."""
    test: dict[str, str] = {"apple": "red"}
    assert invert(test) == {"red": "apple"}


def test_invert_long() -> None:
    """Invert a long dictionary of items."""
    test: dict[str, str] = {"apple": "red","banana": "yellow", "strawberry": "pink"}
    assert invert(test) == {"red": "apple", "yellow": "banana", "pink": "strawberry"}


def test_invert_empty() -> None:
    """Return an error empty dictionary."""
    """edge case."""
    test: dict[str, str] = {}
    assert invert(test) == {}


def test_favorite_color_short() -> None:
    """return the common color of short dictionary."""
    test: dict[str, str] = {"Alan": "blue", "George": "red", "Sam": "blue"}
    assert favorite_color(test) == "blue"


def test_favorite_color_long() -> None:
    """returns the common color of a long dictionary."""
    test: dict[str, str] = {"Alan": "green", "George": "blue", "Sam": "green", "Dan": "yellow", "Sara": "green"}
    assert favorite_color(test) == "green"


def test_favorite_color_empty() -> None:
    """Returns an empty dictionary."""
    """edge case."""
    test: dict[str, str] = {}
    assert favorite_color(test) == ""


def test_count_empty() -> None:
    """Counting how many times a value appears in a dicitionary."""
    """Edge case"""
    test: dict[str, int] = {}
    assert count(test) == {}


def test_