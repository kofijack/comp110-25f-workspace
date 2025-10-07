"""practice with for-in loops"""


def celebrate(pet_names: list[str]) -> None:
    """Tell every pet they're a good boy"""
    for pet in pet_names:
        print(f"Good boy {pet}!")


buddies: list[str] = ["Bear", "Bo", "Louie"]
celebrate(buddies)

# goes with dictionaries fucntion
names: list[str] = ["Alyssa", "Janet", "Vrinda"]
for index in range(0, len(names)):
    print(f"{index}: {names[index]}")
