"""EX03 - Wordle Due: Thursday, October 3"""

__author__: str = "730771829"


def input_guess(secret_word_len: int) -> str:
    """This will prompt the user to input a 5-letter word"""
    while True:
        guess = input(f"Enter a {secret_word_len} character word: ")

        # it will only proceed if the guess provided is the correct length
        if len(guess) == secret_word_len:
            return guess
        else:
            print(f"That wasn't {secret_word_len} chars! Try again.")


def contains_char(word: str, char_guess: str) -> bool:
    """This will see if char_guess is in the word"""

    assert len(char_guess) == 1, "char_guess must be a single character."

    i = 0
    while i < len(word):
        if word[i] == char_guess:
            return True
        i += 1

    return False


def emojified(guess: str, secret: str) -> str:
    assert len(guess) == len(secret)

    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    result: str = ""
    i: int = 0

    # we will use an elif statement to condense the code here
    while i < len(guess):
        if guess[i] == secret[i]:
            result += GREEN_BOX
        elif contains_char(secret, guess[i]):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
        i += 1

    return result


# the f and fancy brackets will tell the code that it must evaluate a value in that area
def main(secret: str) -> None:
    max_turns: int = 6
    turns: int = 1

    while turns <= max_turns:
        print(f"=== Turn {turns}/{max_turns} ===")

        guess: str = input_guess(len(secret))

        emoji_result: str = emojified(guess, secret)
        print(emoji_result)

        if guess == secret:
            print(f"You won in {turns}/{max_turns} turns!")
            return

        turns += 1

    print(f"X/{max_turns} - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
