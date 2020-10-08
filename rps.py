# Rock, paper, scissors.


import random


# Game symbols.
ROCK = 1
PAPER = 2
SCISSORS = 3


# Mappings between different representations of game symbols.
CHAR_2_INT = { "r": ROCK, "p": PAPER, "s": SCISSORS }
INT_2_WORD = { ROCK: "rock", PAPER: "paper", SCISSORS: "scissors"}


# All possible game outcomes and associated message for player.
OUTCOMES = {
    (ROCK, ROCK): "Draw!",
    (PAPER, PAPER): "Draw!",
    (SCISSORS, SCISSORS): "Draw!",
    (ROCK, SCISSORS): "Rock blunts scissors. You win!",
    (PAPER, ROCK): "Paper wraps rock. You win!",
    (SCISSORS, PAPER): "Scissors cut paper. You win!",
    (ROCK, PAPER): "Paper wraps rock. You lose!",
    (PAPER, SCISSORS): "Scissors cut paper. You lose!",
    (SCISSORS, ROCK): "Rock blunts scissors. You lose!"
}


def main():
    play_again = "y"
    while play_again == "y":
        comp_choice = random.randint(1,3)
        player_choice = ""
        while player_choice not in ['r', 'p', 's']:
            player_choice = input("(r)ock, (p)aper, or (s)cissors? ")
        print(INT_2_WORD[CHAR_2_INT[player_choice]], end=" vs ")
        print(INT_2_WORD[comp_choice])
        outcome = OUTCOMES[(CHAR_2_INT[player_choice], comp_choice)]
        print(outcome)
        play_again = input("Play again? [y/n] ")


if __name__ == "__main__":
    main()
