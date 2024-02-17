import random

def guess_the_number():
    number_to_guess = random.randint(1, 20)
    print("Hello! What is your name?")
    name = input()
    print("Well,", name + ", I am thinking of a number between 1 and 20.")

    num_guesses = 0
    while True:
        print("Take a guess.")
        guess = int(input())

        num_guesses += 1

        if guess < number_to_guess:
            print("Your guess is too low.")
        elif guess > number_to_guess:
            print("Your guess is too high.")
        else:
            print("Good job,", name + "! You guessed my number in",num_guesses, "guesses!")
            break

guess_the_number()
