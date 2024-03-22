"""Utils."""
__author__ = "730664950"


def all(my_list: list[int], x: int) -> bool:
    """Are the numbers the same?"""
    if len(my_list) == 0:
        return False
    for elem in my_list:
        if x != elem:
            return False
    return True


def max(input: list[int]) -> int:
    """Returns the highest number in the list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty list")
    max_number = input[0]
    for elem in input:
        if elem > max_number:
            max_number = elem
    return max_number
        

def is_equal(x: list[int], y: list[int]) -> bool:
    """Compares 2 list to see if they are even."""
    if len(x) != len(y):
        return False
    for elem in x and y:
        if x != y:
            return False
    return True


def extend(x: list[int], y: list[int]) -> None:
    """Combines 2 lists provided."""
    x.extend(y)