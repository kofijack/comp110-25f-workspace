__author__: str = "730707796"

"""go through list to identify and remove the largerst number"""


def find_and_remove_max(items: list[int]) -> int:
    if len(items) == 0:
        return -1
    max_num = max(items)
    while max_num in items:
        items.remove(max_num)
    return max_num
