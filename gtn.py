# Guess the number game. From Exercises for Programmers.


import random


# Difficulty levels and associated maximum number.
DIFFICULTY_MAP = {
    1: 10,
    2: 100,
    3: 1000
}


def get_difficulty_level():
    """Prompt the user for a valid difficulty level."""
    level = 0
    while level < 1 or level > 3:
        raw = input("Pick a difficulty level (1, 2, or 3): ")
        try:
            level = int(raw)
        except ValueError:
            pass
    return level


def get_guess(prompt):
    """Get a guess from the user. Invalid input is returned as zero (0)."""
    guess = 0
    raw = input(prompt)
    try:
        guess = int(raw)
    except ValueError:
        pass
    return guess


def determine_outcome(guess, pick):
    """Determine the outcome of the guess. Display a message on screen."""
    if guess == 0:
        print("Invalid guess. ", end=" ")
    elif guess < pick:
        print("Too low.", end=" ")
    elif guess > pick:
        print("Too high.", end=" ")


def show_comment(total_guesses):
    """Display a comment based on the number of guesses."""
    if total_guesses == 1:
        print("You're a mind reader!")
    elif total_guesses >= 2 and total_guesses <= 3:
        print("Most impressive.")
    elif total_guesses >= 4 and total_guesses <= 6:
        print("Not bad.")
    else:
        print("Better luck next time!")


def main():
    print("Let's play Guess the Number.")
    level = get_difficulty_level()
    pick = random.randint(1, DIFFICULTY_MAP[level])
    print(f"I have my number, between 1 and {DIFFICULTY_MAP[level]}.", end=" ")
    total_guesses = 0
    guess = get_guess("What's your guess? ")
    total_guesses += 1
    determine_outcome(guess, pick)
    while not guess == pick:
        guess = get_guess("Guess_again: ")
        total_guesses += 1
        determine_outcome(guess, pick)
    print(f"You got it in {total_guesses} guesses!")
    show_comment(total_guesses)


if __name__ == "__main__":
    main()
