"""cq02_conditionals Due: Friday, September 13"""

__author__: str = "730771829"


def guess_a_number() -> None:
    """has no input and no return type but guesses a number"""
    secret: int = 7
    guess: int = int(input("Guess a number: "))
    if guess == secret:
        print("Your guess was " + str(guess))
        print("You got it!")
    elif guess < secret:
        print("Your guess was " + str(guess))
        print("Your guess was too low! The secret number is 7")
    else:
        print("Your guess was " + str(guess))
        print("Your guess was too high! The secret number is 7")


if __name__ == "__main__":
    guess_a_number()
