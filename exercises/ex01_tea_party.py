"""Simplifying programs into smaller functions that solver a larger problem."""

__author__: str = "730707796"


def tea_bags(people: int) -> int:
    """define tea_bag function"""
    return people * 2


# have to call tea_bags function by referring to it as tea
def treats(people: int) -> int:
    """define treats function"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """define a function to find the total cost of the tea bags and treats"""
    return (tea_count * 0.5) + (treat_count * 0.75)


# make sure to create numtreats and numtea or it would be too long
# f string with {} is necessary with the integer in the string
def main_planner(guests: int) -> None:
    """define a function to combine all functions and see all outputs in one place"""
    print(f"A Cozy Tea Party for {guests} People!")
    print(f"Tea Bags: {tea_bags(people=guests)}")
    print(f"Treats: {treats(people=guests)}")
    print(
        f"Cost: ${cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))}"
    )


# has to be at the end
if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
