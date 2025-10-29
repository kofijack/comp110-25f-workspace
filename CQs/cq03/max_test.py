__author__: str = "730707796"

"""testing the find_and_remove_max finction"""

from CQs.cq03.find_max import find_and_remove_max

"""test that the function is returning the right number"""


def test_returns_expected_value():
    items = [3, 23, 53, 15, 29, 53]
    result = find_and_remove_max(items)
    assert result == 53


"""test that the function is moving the largest number"""


def test_mutates_input():
    items = [3, 23, 53, 15, 29, 53]
    find_and_remove_max(items)
    assert items == [3, 23, 15, 29]


"""namkes sure that if all maxes have been removed, fuction returns -1"""


def test_empty_list():
    items = []
    result = find_and_remove_max(items)
    assert result == -1
    assert items == []
