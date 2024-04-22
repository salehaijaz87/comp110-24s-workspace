"""Challenge question #8 for object oriented programming."""

from __future__ import annotations


class Point:
    """A class."""
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        """Initialize the Point object with given x and y coordinates."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Scale_by function."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """Scale function."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point