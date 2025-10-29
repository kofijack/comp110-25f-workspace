"""Unit test function practice."""

__author__ = "730707796"

from exercises.ex04.dictionary import (
    invert,
    favorite_color,
    count,
    alphabetizer,
    update_attendance,
)


def test_invert_with_pairs() -> None:
    """Function should invert the key and value for both tests."""
    source = {"ten": "10", "nine": "9"}
    assert invert(source) == {"10": "ten", "9": "nine"}


def test_invert_with_words() -> None:
    """Function should invert the key and value for both tests."""
    source = {"never": "nunca", "sometimes": "a veces"}
    assert invert(source) == {"nunca": "never", "a veces": "sometimes"}


def test_invert_empty_dict() -> None:
    """Function should return empty dictionary when given empty dictionary."""
    assert invert({}) == {}


def test_favorite_color_most_popular() -> None:
    """Function should return most popular color."""
    colors = {"Kofi": "green", "Jim": "blue", "Mia": "green", "Lili": "purple"}
    assert favorite_color(colors) == "green"


def test_favorite_color_unique() -> None:
    """Fuction should return the first color if all are unique."""
    colors = {"Ava": "red", "Ben": "yellow", "Cal": "blue"}
    assert favorite_color(colors) == "red"


def test_favorite_color_same() -> None:
    """If same color is chosen by everyone, fucntion should return that color."""
    colors = {"A": "yellow", "B": "yellow", "C": "yellow"}
    assert favorite_color(colors) == "yellow"


def test_count_word_replication() -> None:
    """Function should count how many times a word appears."""
    words = ["night", "day", "day", "afternoon", "night"]
    assert count(words) == {"night": 2, "day": 2, "afternoon": 1}


def test_count_all_different() -> None:
    """Each word should appear once."""
    words = ["day", "afternoon", "night"]
    assert count(words) == {"day": 1, "afternoon": 1, "night": 1}


def test_count_same() -> None:
    """If all items are the same, the fucntion should return one key."""
    assert count(["spoon", "spoon", "spoon"]) == {"spoon": 3}


def test_alphabetizer_normal_case() -> None:
    """Group words by first letter even if some aren't capitalized."""
    words = ["Apple", "avocado", "Banana", "berry", "cherry"]
    assert alphabetizer(words) == {
        "a": ["Apple", "avocado"],
        "b": ["Banana", "berry"],
        "c": ["cherry"],
    }


def test_alphabetizer_same_letter() -> None:
    """All words with the same first letter should go in a group."""
    words = ["lake", "lunch", "life"]
    assert alphabetizer(words) == {"l": ["lake", "lunch", "life"]}


def test_alphabetizer_dif_start() -> None:
    """Function should skip words that start with symbols or numbers."""
    words = ["*multiply", "/divide", "add"]
    assert alphabetizer(words) == {"a": ["add"]}


def test_update_attendance_add_day_and_students() -> None:
    """Function should add a day and students on that day."""
    attendance: dict[str, list[str]] = {}
    update_attendance(attendance, "Friday", "Frank")
    assert attendance == {"Friday": ["Frank"]}


def test_update_attendance_add_to_existing() -> None:
    """Function should add student to existing day without removing others."""
    attendance = {"Wednesday": ["Ella"]}
    update_attendance(attendance, "Wednesday", "Kai")
    assert attendance == {"Wednesday": ["Ella", "Kai"]}


def test_update_attendance_multiple_days() -> None:
    """Function should add students to different days without overwriting."""
    attendance = {"Monday": ["Milly"]}
    update_attendance(attendance, "Tuesday", "Ben")
    assert attendance == {"Monday": ["Milly"], "Tuesday": ["Ben"]}
