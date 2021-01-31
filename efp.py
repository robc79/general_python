# Exercises for programmers.


import datetime


def say_hi():
    """Ask for aname from std input and say hello on std output."""
    name = input("What is your name? ")
    print(f"Hello, {name}, nice to meet you.")


def count_chars():
    """Count number of characters in a string supplied on std input."""
    chars = ""
    while chars == "":
        chars = input("What is the input string? ")
    print(f"{chars} has {len(chars)} characters.")


def quote_it():
    """Prompt for a quote and print it out."""
    quote = input("What is the quote? ")
    who = input("Who said it? ")
    print(f'{who} says, "{quote}"')


def quote_lots():
    """Display a set of quotations on std output."""
    quotes = [
        ("Too be, or not to be.", "Hamlet"),
        ("Do be do be do.", "Sinatra"),
        ("Thou art that.", "Unknown")
    ]
    for quote, who in quotes:
        print(f'{who} says, "{quote}"')


def mad_lib():
    """One line mad lib."""
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adjective = input("Enter an adjective: ")
    adverb = input("Enter an adverb: ")
    print(f"Do you {verb} your {adjective} {noun} {adverb}? That's hilarious!")


def add_two():
    """Prompt for two non negative numbers on std input, print out the sum,
    difference, product, and quotient of them."""
    num1 = -1
    while num1 < 0:
        first = input("What is the first number? ")
        try:
            num1 = float(first)
        except ValueError:
            pass
    num2 = -1
    while num2 < 0:
        second = input("What is the second number? ")
        try:
            num2 = float(second)
        except ValueError:
            pass
    print(f"{first} + {second} = {num1 + num2}")
    print(f"{first} - {second} = {num1 - num2}")
    print(f"{first} * {second} = {num1 * num2}")
    if num2 == 0:
        print("Cannot divide by zero.")
    else:
        print(f"{first} / {second} = {num1 / num2}")


def retire():
    """Prompt for an age and a retirement age, show how many years left till
    retirement."""
    age = input("What is your current age? ")
    retire_age = input("At what age would you like to retire? ")
    years_left = int(retire_age) - int(age)
    print(f"You have {years_left} years left until you can retire.")
    year = datetime.date.today().year
    retire_year = year + years_left
    print(f"It's {year}, so you can retire in {retire_year}.")


def area_of_room():
    """Prompt for two non-negative integers on std input. Show the area of them
    in feet and meteers squared."""
    CONVERSION_FACTOR = 0.09290304
    length = -1
    while length < 0:
        raw_length = input("What is the length of the room in feet? ")
        try:
            length = int(raw_length)
        except ValueError:
            pass
    width = -1
    while width < 0:
        raw_width = input("What is the width of the room in feet? ")
        try:
            width = int(raw_width)
        except ValueError:
            pass
    print(f"You entered dimensions of {length} feet by {width} feet.")
    print("The area is")
    area_sqf = length * width
    print(f"{area_sqf} square feet")
    area_sqm = area_sqf * CONVERSION_FACTOR
    print(f"{area_sqm} square meters")


def pizza_party():
    """Calculate the number of slices of pizza each person gets."""
    people = 0
    while people < 1:
        raw_people = input("How many people? ")
        try:
            people = int(raw_people)
        except ValueError:
            pass
    pizzas = 0
    while pizzas < 1:
        raw_pizza = input("How many pizzas do you have? ")
        try:
            pizzas = int(raw_pizza)
        except ValueError:
            pass
    slices_per_pizza = 0
    while slices_per_pizza < 1:
        raw_slices_per_pizza = input("How many slices per pizza? ")
        try:
            slices_per_pizza = int(raw_slices_per_pizza)
        except ValueError:
            pass
    print(f"{people} people with {pizzas} pizzas in {slices_per_pizza} slices")
    total_slices = pizzas * slices_per_pizza
    slices_per_person = total_slices // people
    leftovers = total_slices % people
    print(f"Each person gets {slices_per_person} slices of pizza.")
    print(f"There are {leftovers} leftover slices.")

