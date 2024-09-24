"""EX02 - Chardle - A cute step toward Wordle."""

__author__: str = "730771829"


def input_word() -> str:
    # This will prompt the user for a 5-character word
    word = input("Enter a 5-character word: ")
    # A corresponding "else" is not needed
    if len(word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()

    return word


def input_letter() -> str:
    letter = input("Enter a single character: ")
    # MThis will check if the length of the input for single character is equal to 1
    if len(letter) != 1:
        print("Error: Character must be a single character.")
        exit()

    return letter


def contains_char(word: str, letter: str) -> None:
    print("Searching for " + letter + "in" + word)

    match_count = 0

    # each block does not need its own else branch
    if len(letter) == 1:
        if word[0] == letter:
            print(letter + " found at index 0")
            match_count += 1
        if word[1] == letter:
            print(letter + " found at index 1")
            match_count += 1
        if word[2] == letter:
            print(letter + " found at index 2")
            match_count += 1
        if word[3] == letter:
            print(letter + " found at index 3")
            match_count += 1
        if word[4] == letter:
            print(letter + " found at index 4")
            match_count += 1
    # indentation must be precise here or else code will not run properly
    else:
        print("Error: Character must be a single character.")
    # an elif block can be used to shorten the code and make it easier to read
    # pay attention to spaces and spelling of word
    if match_count == 0:
        print("No instances of " + letter + " found in " + word)
    elif match_count == 1:
        print(str(match_count) + " instance of " + letter + " found in " + word)
    else:
        print(str(match_count) + " instances of " + letter + " found in " + word)


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
