# Hangman.

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
    return letter[0]


word = "cat" # TODO: read this from a list of common words (part 2).
guessed_letters = []
incorrect_letters = []


# Game loop.
MAX_WRONG_GUESSES = 5

while len(guessed_letters) != len(word) and len(incorrect_letters) < MAX_WRONG_GUESSES:
    show_word(word, guessed_letters)
    show_wrong_guesses(incorrect_letters)
    letter = get_letter()
    if letter in word and letter not in guessed_letters:
        guessed_letters.append(letter)
    elif letter not in incorrect_letters:
        incorrect_letters.append(letter)

# End of game message.
if len(guessed_letters) == len(word):
    show_word(word, guessed_letters)
    print(f"Well done! You guessed the word with {len(incorrect_letters)} wrong guesses.")
else:
    print(f"Too many wrong guesses! The word was '{word}'")
