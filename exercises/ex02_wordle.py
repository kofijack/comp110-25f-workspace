__author__: str = "730707796"


"""ensures that the guess made is 5 characters long"""


def input_guess(expected_length: int) -> str:
    guess = input(f"Enter a {expected_length} character word: ")
    while (
        len(guess) != expected_length
    ):  # wont allow user to continue until guess is 5 characters
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess


"""tells user if any letter from the word they guess are in the actual word"""


def contains_char(word: str, letter_match: str) -> bool:
    assert len(letter_match) == 1, f"len('{letter_match}') is not 1"
    for letter in word:
        if letter == letter_match:
            return True
    return False  # don't need an else statement, just return


WHITE_BOX: str = "\U00002b1c"
GREEN_BOX: str = "\U0001f7e9"
YELLOW_BOX: str = "\U0001f7e8"

"""assigns color to letters of word guessed"""


def emojified(guess: str, secret: str) -> str:
    assert len(guess) == len(secret), "Guess must be same length as secret"
    result = ""
    for i in range(len(guess)):
        if guess[i] == secret[i]:
            result += GREEN_BOX
        elif contains_char(secret, guess[i]):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
    return result  # make sure not to leave out indent


"""combines previous functions into main wordle function"""


def main(secret: str) -> None:
    turn = 1
    max_turns = 6
    won = False

    while turn <= max_turns and not won:
        print(f"=== Turn {turn}/{max_turns} ===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            won = True
            print(f"You won in {turn}/{max_turns} turns!")
        else:
            turn += 1  # need to make sure loop doesn't run forever
    if not won:
        print(f"X/{max_turns} - Sorry, try again tomorrow!")


"""allows the game to actually run"""


if __name__ == "__main__":
    main(secret="codes")
