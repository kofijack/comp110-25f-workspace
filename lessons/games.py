"""Definition of Games class"""


class Games:

    collection: list[str]
    wishlist: list[str]
    budget: float

    def __init__(
        self, curr_collection: list[str], wish: list[str], start_budget: float
    ):
        self.collection = curr_collection
        self.wishlist = wish
        self.budget = start_budget

    def purchase(self, name: str, cost: float):
        if cost < self.budget:
            self.budget -= cost
            self.collection.append(name)
            game_idx: int = 0
            while game_idx < len(self.wishlist):
                if self.wishlist[game_idx] == name:
                    self.wishlist.pop(game_idx)
                game_idx += 1
        else:
            print("Sorry! Not enough money!")


my_games: Games = Games(["Sims"], ["Witcher"], 50.75)
my_games.purchase("Stardew", 40.25)
print(my_games.collection)
print(my_games.budget)
my_games.purchase("Witcher", 60.00)
print(my_games.collection)
print(my_games.wishlist)
