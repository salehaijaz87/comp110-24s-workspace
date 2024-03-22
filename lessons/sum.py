"""Summing the elements of a list using different loops."""

__author__: "730664950"


def w_sum(vals: list[float]) -> float:
    index: int = 0
    sum_list: float = 0.0
    while index < len(vals):
        sum_list += vals[index]
        index += 1
    return sum_list


def f_sum(vals: list[float]) -> float:
    index: int = 0
    sum_list: float = 0.0
    for elem in vals:
        sum_list += elem
    return sum_list


def f_range_sum(vals: list[float]) -> float:
    index: int = 0
    sum_list: float = 0.0
    for index in range(0, len(vals)):
        sum_list += vals[index]
    return sum_list