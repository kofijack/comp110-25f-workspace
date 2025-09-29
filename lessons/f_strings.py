"""Practice with f-strings and positional arguments"""


def get_class(subject: str, num: int) -> None:
    print(f"I'm taking {subject} {num}.")


# make sure NOT to indent call
get_class("COMP", 110)
