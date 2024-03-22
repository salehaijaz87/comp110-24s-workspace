"""Test my garden functions."""

__author__: "730664950"
from lessons.garden.garden_helpers import add_by_kind
from lessons.garden.garden_helpers import add_by_date
from lessons.garden.garden_helpers import lookup_by_kind_and_date

def test_add_by_kind_correct() -> None:
    """Adds new item to the list in dictionary."""
    dict_1: dict[str, list[str]] = {"fruit": ["orange"]}
    add_by_kind(dict_1, "fruit", "apple")
    assert dict_1 == {"fruit": ["orange", "apple"]}

def test_add_by_kind_empty() -> None:
    """Adding nothing to the list in dcitiosnary"""
    