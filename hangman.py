# Hangman.

MAX_INCORRECT_LETTERS = 5


def show_word(word, letters):
    print("Word: ", end="")
    for c in word:
        if c in letters:
            print(c, end="")
        else:
            print("-", end="")
    print()


word = "something" # TODO: read this from a list of common words (part 2).
guessed_letters = []
incorrect_letters = []


# Game loop.
while len(guessed_letters) != len(word) and len(incorrect_letters) < MAX_INCORRECT_LETTERS:
    show_word(word, guessed_letters)
    print("Wrong guesses: ", end="")
    for l in incorrect_letters:
        print(l, end="")
    print()
    picked_letter = ""
    while picked_letter == "":
        picked_letter = input("Guess a letter > ")
        picked_letter = picked_letter[0]
    if picked_letter in word:
        guessed_letters.append(picked_letter)
    else:
        incorrect_letters.append(picked_letter)
# End of game message.
if len(guessed_letters) == len(word):
    show_word(word, guessed_letters)
    print("Well done! You guessed the word with {} wrong guesses.".format(
        len(incorrect_letters)))
else:
    print(f"Too many wrong guesses! The word was '{word}'")
