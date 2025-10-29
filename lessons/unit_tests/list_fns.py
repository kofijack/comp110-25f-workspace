def get_first(items: list[str]) -> str:
    if len(items) == 0:
        return ""
    return items[0]


def remove_first(items: list[str]) -> None:
    items.pop(0)


def get_and_remove_first(items: list[str]) -> str:
    first: str = items[0]
    items.pop(0)
    return first
