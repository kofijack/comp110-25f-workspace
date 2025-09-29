"""Paracticing list syntax"""

# Create an empty list of floats called my_numbers
my_numbers: list[float] = list()  # <- constructor
my_numbers: list[float] = []  # <- literal
print(my_numbers)

# Add the value 1.5 to my_numbers
my_numbers.append(1.5)
print(my_numbers)

# Create an already populated list
game_points: list[int] = [102, 86, 94]
print(game_points)

# Acccess elemetn of list using subscription notation
print(game_points[2])

# Modify element of a list
game_points[1] = 72
print(game_points)
print(len(game_points))

# remove an element
print(game_points.pop(1))  # returns the item that you're removing
