"""ex01_tea_party Due: Thursday, September 12"""

__author__: str = "730771829"


# The print statements here are based on what was on the Comp website.
def main_planner(guests: int) -> None:
    """Prints total output, entrypoint to the program"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=(treats(people=guests)))
        )
    )


# No math should be happening in main_planner.


def tea_bags(people: int) -> int:
    """Number of tea bags needed based on number of people attending"""
    return people * 2


def treats(people: int) -> int:
    """Number of treats needed based on number of people attending"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """will return total cost of tea bags and treats combined"""
    return tea_count * 0.50 + treat_count * 0.75


# This next bit of code makes the program runnable.

if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
