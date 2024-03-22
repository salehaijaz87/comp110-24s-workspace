"""Dictionary."""

__author__ = "730664935"


def invert(x: dict[str, str]) -> dict[str, str]:
    """Inverts the numbers provided."""
    new_dict: dict[str, str] = {}
    for key in x:
        if x[key] in new_dict:
            raise KeyError("error! Cannot be inverted.")
        else: 
            new_dict[x[key]] = key
    return (new_dict)


def favorite_color(x: dict[str, str]) -> str:
    """Prints the overall color."""
    new_dict: dict[str, int] = {}
    popular_color: str = ""
    max_count: int = 0
    for key in x:
        color = x[key]
        if color in new_dict:
            new_dict[color] += 1
        else:
            new_dict[color] = 1
        if new_dict[color] > max_count:
            popular_color = color
            max_count = new_dict[color]
    return popular_color


def count(x: list[str]) -> dict[str, int]:
    """Count the number of times a value appears."""
    new_dict: dict[str, int] = {}
    for key in x:
        if key in new_dict:
            new_dict[key] += 1
        else:
            new_dict[key] = 1
    return new_dict


def alphabetizer(x: list[str]) -> dict[str, list[str]]:
    """Alphabetilize the inputs."""
    new_dict: dict[str, list[str]] = {}
    for key in x:
        first_letter = key[0].lower()
        if first_letter in new_dict:  # If the first letter is already in the new_dict, we append to add word to the list.
            new_dict[first_letter].append(key)
        else: 
            new_dict[first_letter] = [key]
    return new_dict


def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> None:
    """Update attendace."""
    if day in attendance: 
        if student not in attendance[day]:
            attendance[day].append(student)
    else:
        attendance[day] = [student]