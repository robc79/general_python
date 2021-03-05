# Implementation of FizzBuzz.

def fizz_buzz(num):
    isFizz = num % 3 == 0
    isBuzz = num % 5 == 0
    if isFizz and isBuzz:
        word = "FizzBuzz"
    elif isFizz:
        word = "Fizz"
    elif isBuzz:
        word = "Buzz"
    else:
        word = str(num)
    return word


if __name__ == "__main__":
    for i in range(1, 100):
        print(fizz_buzz(i), end=" ")
