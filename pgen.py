# Password generator.

import random


NOISE = "!#?$%"
NUMBERS = "1234567890"


word_list = []


def load_word_list(filename):
    with open(filename) as f:
        lines = f.readlines()
    for line in lines:
        n_line = line[:-1].capitalize()
        if len(n_line) > 3:
            word_list.append(n_line)


def _word_pair(words):
    l = len(words) - 1
    i = random.randint(0, l)
    j = random.randint(0, l)
    return (words[i], words[j])


def _salt():
    s = []
    r = random.randint(1,2)
    t = 3 - r
    for i in range(r):
        s.append(NUMBERS[random.randint(0, len(NUMBERS)-1)])
    for i in range(t):
        s.append(NOISE[random.randint(0, len(NOISE)-1)])
    return "".join(s)


def password(words = word_list):
    """Generate a password from the supplied word list."""
    p = _word_pair(words)
    s = _salt()
    return f"{p[0]}{p[1]}{s}"
