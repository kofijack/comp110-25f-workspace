from lessons.unit_tests.list_fns import get_first, remove_first


def test_get_first_use_case() -> None:
    """check that get_first returns first element, "chair"."""
    example: list[str] = ["chair", "desk" "lamp"]
    assert get_first(example) == "chair"


def test_get_first_edge_case() -> None:
    """check that get_ first returns empty string when given empty list"""
    example: list[str] = []
    get_first(example)
    assert get_first(example) == ""


def test_remove_first_use_case() -> None:
    """check that remove_first removes the first element"""
    example: list[str] = ["chair", "desk", "lamp"]
    remove_first(example)
    assert example == ["desk", "lamp"]
