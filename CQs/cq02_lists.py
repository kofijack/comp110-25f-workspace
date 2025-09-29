"""Mutating Fuctions"""

__author__: str = "730707796"


def manual_append(input_list: list[int], input_value: int) -> None:
    input_list.append(input_value)


def double(numbers: list[int]) -> None:
    i: int = 0
    while i < len(numbers):
        numbers[i] *= 2
        i += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)

print(list_1)
print(list_2)
