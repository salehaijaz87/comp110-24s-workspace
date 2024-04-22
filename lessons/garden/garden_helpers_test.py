"""Test my garden functions."""
from lessons.garden.garden_helpers import add_by_kind
from lessons.garden.garden_helpers import add_by_date
from lessons.garden.garden_helpers import lookup_by_kind_and_date

__author__: "730664950"


def test_add_by_kind_normal_input() -> None:
    """Adds new item to the list in dictionary."""
    plants_by_kind: dict[str, list[str]] = {"vegetable": ["tomato"]}
    plant_kind: str = "vegetable"
    plant: str = "carrot"
    add_by_kind(plants_by_kind, plant_kind, plant)  # Calling the functions
    assert plants_by_kind == {"vegetable": ["tomato", "carrot"]}


def test_add_by_kind_empty_list() -> None:
    """Adding item to empty list."""
    plants_by_kind: dict[str, list[str]] = {"vegetable": []}
    plant_kind: str = "vegetable"
    plant: str = "carrot"
    add_by_kind(plants_by_kind, plant_kind, plant)
    assert plants_by_kind == {"vegetable": ["carrot"]}


def test_add_by_date_normal_input() -> None:
    """Adds item to an existing month."""
    plants_by_date: dict[str, list[str]] = {"June": ["rose"]}
    month: str = "June"
    plant: str = "sunflower"
    add_by_date(plants_by_date, month, plant)
    assert plants_by_date == {"June": ["rose", "sunflower"]}


def test_add_by_date_new() -> None:
    """Adds item to a month that has an empty list."""
    plants_by_date: dict[str, list[str]] = {"July": []}
    month: str = "July"
    plant: str = "sunflower"
    add_by_date(plants_by_date, month, plant)
    assert plants_by_date == {"July": ["sunflower"]}


def test_lookup_by_kind_and_date_normal_input() -> None:
    """Test the function with normal input."""
    plants_by_kind: dict[str, list[str]] = {"flower": ["tulip"], "fruit": ["orange"]}
    plants_by_date: dict[str, list[str]] = {"June": ["tulip", "orange"]}
    plant_kind: str = "fruit"
    month: str = "June"
    x = lookup_by_kind_and_date(plants_by_kind, plants_by_date, plant_kind, month) 
    assert x == "fruits to plant in June: ['orange']"


def test_lookup_by_kind_and_date_empty() -> None:
    """Test the function with an empty input."""
    plants_by_kind: dict[str, list[str]] = {"fruit": [], "flower": ["tulip"]}
    plants_by_date: dict[str, list[str]] = {"June": ["tulip"]}
    plant_kind: str = "fruit"
    month: str = "June"
    x = lookup_by_kind_and_date(plants_by_kind, plants_by_date, plant_kind, month) 
    assert x == "No fruit to plant in June"
