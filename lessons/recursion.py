"""Recursion challenge question."""
__author__ = "730664950"


def f(n: int, k: int) -> int:
    """Recursive rule."""
    if n == 0: 
        return 0
    else: 
        return f(n - 1, k) + k
