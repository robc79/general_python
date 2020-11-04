# Hangman.

MAX_WRONG_GUESSES = 5


def show_word(word, letters):
    print("Word: ", end="")
    for letter in word:
        if letter in letters:
            print(letter, end="")
        else:
            print("-", end="")
    print()


def show_wrong_guesses(guesses):
    print("Wrong guesses: ", end="")
    for letter in guesses:
        print(letter, end="")
    print()


def get_letter():
    letter = ""
    while letter == "":
        letter = input("Guess a letter > ")
        if letter != "":
            letter = letter[0]
    return letter


word = "something" # TODO: read this from a list of common words (part 2).
guessed_letters = []
incorrect_letters = []


# Game loop.
while len(guessed_letters) != len(word) and len(incorrect_letters) < MAX_WRONG_GUESSES:
    show_word(word, guessed_letters)
    show_wrong_guesses(incorrect_letters)
    letter = get_letter()
    if letter in word and letter not in guessed_letters:
        guessed_letters.append(letter)
    elif letter not in word and letter not in incorrect_letters:
        incorrect_letters.append(letter)
# End of game message.
if len(guessed_letters) == len(word):
    show_word(word, guessed_letters)
    print("Well done! You guessed the word with {} wrong guesses.".format(
        len(incorrect_letters)))
else:
    print(f"Too many wrong guesses! The word was '{word}'")
