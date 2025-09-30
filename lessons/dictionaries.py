"""practice with basic dictionary syntax"""

ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}
print(ice_cream)

# add an element
ice_cream["mint"] = 3
print(ice_cream)

# remove an element
ice_cream.pop("mint")
print(ice_cream)

# access
print(ice_cream["chocolate"])

# update
ice_cream["vanilla"] += 2
ice_cream["vanilla"] = 10

# length
print(len(ice_cream))

# check if element is in dictionary
print("mint" in ice_cream)

if "mint" in ice_cream:
    print(ice_cream["mint"])
else:
    print("no orders of mint")


def grade_bump(gradebook: dict[str, str], student: str) -> None:
    """Bump up students grade"""
    if gradebook[student] == "A":
        gradebook[student] == "A+"
    else:
        gradebook[student] == "A"


grades: dict[str, str] = {"kofi": "A", "luke": "B"}
grade_bump(grades, "kofi")
print(grades)
grade_bump(grades, "luke")
print(grades)
