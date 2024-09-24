"""cq03_while_loops Due: Wednesday, September 18"""

__author__: str = "730771829"


def num_instances(phrase: str, search_char: str) -> int:
    """the num_instances function will tell us how many times the phrase occurs"""
    count: int = 0
    instances: int = 0
    """created a new variable called instances to see how many times it happened"""
    while count < len(phrase):
        if search_char == phrase[count]:
            instances = instances + 1
        count = count + 1
    return instances
    """Not returning the function here,returning instances so that it executes a loop"""
