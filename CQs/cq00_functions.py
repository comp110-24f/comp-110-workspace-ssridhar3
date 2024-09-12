"""CQ00"""

__author__ = "730771829"


def mimic(message: str) -> str:
    """The function should simply return message back to you!"""
    return message


def main() -> None:
    """Print the results of the mimic function"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
