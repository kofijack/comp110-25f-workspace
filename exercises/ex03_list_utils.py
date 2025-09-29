"""list utility function reproduction for practice"""

__author__: str = "730707796"


"""checking that all numbers in a list equal the one correct number"""


def all(numbers: list[int], number: int) -> bool:

    storage: list[int] = []
    result: bool = True

    if len(numbers) == 0:
        return False
    while len(numbers) > 0:  # need to have fuction run until there are no numbers left
        current = numbers.pop()  # used to remove number from list
        if current != number:
            result = False
        storage.append(current)
    while len(storage) > 0:
        numbers.append(storage.pop())  # going back to original
    return result


"""getting the largest number from list"""


def max(numbers: list[int]) -> int:

    storage: list[int] = []
    largest = numbers.pop()
    storage.append(largest)

    if len(numbers) == 0:
        raise ValueError("max() arg is an empty List")
    while len(numbers) > 0:
        elem = numbers.pop()
        if elem > largest:  # goes through numbers to find largest
            largest = elem
        storage.append(elem)
    while len(storage) > 0:
        numbers.append(storage.pop())
    return largest  # make sure to call varibale largest instead of funtion max


"""checks that two lists have the same numbers in the same order"""


def is_equal(list1: list[int], list2: list[int]) -> bool:

    storage1: list[int] = []
    storage2: list[int] = []
    result: bool = True

    if len(list1) != len(list2):
        return False
    while len(list1) > 0:
        number1 = list1.pop()
        number2 = list2.pop()
        if number1 != number2:
            result = False
        storage1.append(number1)
        storage2.append(number2)
    while len(storage1) > 0:  # both lists back to original
        list1.append(storage1.pop())
        list2.append(storage2.pop())
    return result


"""extending a list by adding another lists values to the end of the first list"""


def extend(list1: list[int], list2: list[int]) -> None:

    storage: list[int] = []  # need to temporarily hold the numbers

    while len(list2) > 0:
        storage.append(list2.pop())  # specifies that numbers are being taken from list2
    while len(storage) > 0:
        number = storage.pop()
        list1.append(number)
        list2.append(number)
