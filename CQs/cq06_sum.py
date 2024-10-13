"""Summing the elements of a list using different loops"""

__author__: str = "730771829"


# Part 1: w_sum using while loop
def w_sum(vals: list[float]) -> float:
    total = 0.0
    index = 0
    while index < len(vals):
        total += vals[index]
        index += 1
    return total


# Part 2: f_sum using for...in loop
def f_sum(vals: list[float]) -> float:
    total = 0.0
    for val in vals:
        total += val
    return total


# Part 3: f_range_sum using for...in range(...) loop
def f_range_sum(vals: list[float]) -> float:
    total = 0.0
    for i in range(len(vals)):
        total += vals[i]
    return total
