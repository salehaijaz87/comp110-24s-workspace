"""Testing my functions from dictionary."""
from exercises.ex05.dictionary import invert
from exercises.ex05.dictionary import favorite_color
from exercises.ex05.dictionary import count
from exercises.ex05.dictionary import alphabetizer
from exercises.ex05.dictionary import update_attendance

__author__: "730664950"


def test_invert_short() -> None:
    """Invert a short dictionary of items."""
    test: dict[str, str] = {"apple": "red"}
    assert invert(test) == {"red": "apple"}


def test_invert_long() -> None:
    """Invert a long dictionary of items."""
    test: dict[str, str] = {"apple": "red", "banana": "yellow", "strawberry": "pink"}
    assert invert(test) == {"red": "apple", "yellow": "banana", "pink": "strawberry"}


def test_invert_empty() -> None:
    """Return an error empty dictionary."""
    """edge case."""
    test: dict[str, str] = {}
    assert invert(test) == {}


def test_favorite_color_short() -> None:
    """Return the common color of short dictionary."""
    test: dict[str, str] = {"Alan": "blue", "George": "red", "Sam": "blue"}
    assert favorite_color(test) == "blue"


def test_favorite_color_long() -> None:
    """Returns the common color of a long dictionary."""
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
    test: list[str] = []
    assert count(test) == {}


def test_count_long() -> None:
    """Count the number of times a value appear within a long list."""
    test: list[str] = ["a", "a", "d", "c", "b", "a", "d", "b", "c"]
    assert count(test) == {"a": 3, "b": 2, "c": 2, "d": 2}


def test_count_short() -> None:
    """Count the # of times a value appears within a short list."""
    test: list[str] = ["a", "a", "b"]
    assert count(test) == {"a": 2, "b": 1}


def test_alphabetizer_empty() -> None:
    """Test the function when empty input is given."""
    """Edge case."""
    test: list[str] = []
    assert alphabetizer(test) == {}


def test_alphabetizer_short() -> None:
    """Test function when short input is given."""
    test: list[str] = ["Alice", "Aaron", "Betsy", "Bob"]
    assert alphabetizer(test) == {"a": ["Alice", "Aaron"], "b": ["Betsy", "Bob"]}


def test_alphabetizer_long() -> None:
    """Test the fucntion when long input is given."""
    test: list[str] = ["Sam", "Saleha", "Emma", "Sara", "Katie", "Kierra", "Erika", "Kaden"]
    assert alphabetizer(test) == {"e": ["Emma", "Erika"], "k": ["Katie", "Kierra", "Kaden"], "s": ["Sam", "Saleha", "Sara"]}


def test_update_attendance_short() -> None:
    """Test the function when a short input is given."""
    attendace_test: dict[str, list[str]] = {}
    day: str = "Monday"
    student: str = "Amy"
    update_attendance(attendace_test, day, student)  # calling the function to update_attendance
    assert attendace_test == {"Monday": ["Amy"]}


def test_update_attendance_add() -> None:
    """Adds student to attendance."""
    attendace_test: dict[str, list[str]] = {"Monday": ["Sam", "James"]}
    day: str = "Monday"
    student: str = "Jose"
    attendace_test[day].append(student)
    update_attendance(attendace_test, day, student)
    assert attendace_test == {"Monday": ["Sam", "James", "Jose"]}


def test_update_attendance_empty() -> None:
    """Test function with an empty list."""
    attendace_test: dict[str, list[str]] = {"Monday": []}
    day: str = "Monday"
    student: str = "Amy"
    update_attendance(attendace_test, day, student)
    assert attendace_test == {"Monday": ["Amy"]}