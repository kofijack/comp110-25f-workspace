"""Dictionary fucntion practice."""

__author__ = "730707796"


def invert(source: dict[str, str]) -> dict[str, str]:
    """Use a dictionary to invert the keys and values."""
    result: dict[str, str] = {}
    for key in source:
        value = source[key]  # sets value as a variable
        if value in result:
            raise KeyError("Duplicate key found!")  # prevents against same key twice
        result[value] = key
    return result


def favorite_color(pick: dict[str, str]) -> str:
    """Take favorite colors and return the most popular."""
    color_count: dict[str, int] = {}
    for key in pick:
        color = pick[key]
        several: bool = False
        for current_color in color_count:  # counts how many times a color was chosen
            if current_color == color:
                color_count[current_color] += 1
                several = True
        if not several:
            color_count[color] = 1
    max_color: str = ""
    max_count: int = 0
    for key in pick:  # chooses whcih color is most popular
        color = pick[key]
        if color_count[color] > max_count:
            max_color = color
            max_count = color_count[color]
    return max_color


def count(inventory: list[str]) -> dict[str, int]:
    """Count how many times the string is in the list."""
    result: dict[str, int] = {}  # makes sure the dictionary is empty
    for item in inventory:
        if item in result:  # either adds the item to its group or makes new group
            result[item] += 1
        else:
            result[item] = 1
    return result


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Organize a list by first letter."""
    result: dict[str, list[str]] = {}
    for word in words:
        first_letter = word[0].lower()
        if first_letter.isalpha():
            if (
                first_letter in result
            ):  # adds the word to group if it has same first letter
                result[first_letter].append(word)
            else:  # or puts the word by itself
                result[first_letter] = [word]
    return result


def update_attendance(
    attendance_log: dict[str, list[str]], day: str, student: str
) -> None:
    """Changer attendance log to add a stuent to a day."""
    if day in attendance_log:
        if student not in attendance_log[day]:
            attendance_log[day].append(student)  # adds student
    else:
        attendance_log[day] = [student]
