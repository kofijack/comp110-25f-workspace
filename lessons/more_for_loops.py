def for_loop(items: list[str]) -> str:
    """print every element in items and return the last element"""
    for elem in items:
        print(elem)
    return elem


def for_range_loop(items: list[str]) -> str:
    """print every element in items and return the last element"""
    for idx in range(0, len(items)):
        print(items[idx])
    return items[idx]


animals: list[str] = ["monkey", "zebra", "snake"]
print(for_loop(animals))
