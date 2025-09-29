__author__: str = "730707796"


def guess_a_number() -> None:
    """A simple number guessing game"""
    secret: int = 7
    guess: str = input("Guess a number: ")
    x: int = int(guess)
    print("Your guess was", x)
    if x == secret:
        print("You got it!")
    elif x < secret:
        print("Your guess was too low! The secret number is " + str(secret))
    else:
        print("Your guess was too high! The secret number is " + str(secret))


if __name__ == "__main__":
    guess_a_number()
