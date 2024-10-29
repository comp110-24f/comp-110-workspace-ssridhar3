"""ex06_dictionary.py Due: Tuesday, October 29"""

__author__: str = "730771829"


def invert(input: dict[str, str]) -> dict[str, str]:
    """This will invert the keys and values in the dictionary"""
    inverted_dict = {}
    for key, value in input.items():
        if value in inverted_dict:
            raise KeyError("Duplicate values found in the dictionary!")
        inverted_dict[value] = key
    return inverted_dict


def favorite_color(colors_dict: dict[str, str]) -> str:
    """Returns the most frequent color from the dictionary"""
    color_counts = {}
    for color in colors_dict.values():
        color_counts[color] = color_counts.get(color, 0) + 1

    # Find the color with the highest number of appearances
    max_color = ""
    max_count = 0
    for color, count in color_counts.items():
        if count > max_count or (count == max_count and max_color == ""):
            max_color = color
            max_count = count

    return max_color


def count(values: list[str]) -> dict[str, int]:
    """Return a dictionary with counts of each item in the input list"""
    counts_dict = {}
    for item in values:
        if item in counts_dict:
            counts_dict[item] += 1
        else:
            counts_dict[item] = 1
    return counts_dict


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Returns a dictionary after grouping words in alphabetical order"""
    alphabet_dict = {}
    for word in words:
        first_letter = word[0].lower()
        if first_letter not in alphabet_dict:
            alphabet_dict[first_letter] = []
        alphabet_dict[first_letter].append(word)
    return alphabet_dict


def update_attendance(
    attendance_log: dict[str, list[str]], day: str, student: str
) -> None:
    """Updates the attendance log for a specific day with a student's attendance."""
    if day in attendance_log:
        if student not in attendance_log[day]:
            attendance_log[day].append(student)
    else:
        attendance_log[day] = [student]
