#!/bin/python3
# MasterMind
# by ICTROCN
# v1.01
# 15-8-2024
# Last mod by DevJan : added loop for replay
print("MasterMind")

import random

colors = ["red", "blue", "green", "yellow", "orange", "brown"]

def generate_code(length=4, digits=6, use_colors=False):
    if use_colors:
        return [random.choice(colors) for _ in range(length)]
    else:
        return [str(random.randint(1, digits)) for _ in range(length)]

def get_Feedback(secret, guess):
    black_Pegs = sum(s == g for s, g in zip(secret, guess))
    
    # Count whites by subtracting black and calculating min digit frequency match
    secret_Counts = {}
    guess_Counts = {}

    for s, g in zip(secret, guess):
        if s != g:
            secret_Counts[s] = secret_Counts.get(s, 0) + 1
            guess_Counts[g] = guess_Counts.get(g, 0) + 1

    white_Pegs = sum(min(secret_Counts.get(d, 0), guess_Counts.get(d, 0)) for d in guess_Counts)
    
    return black_Pegs, white_Pegs

def show_Secret(mystery):
    print(mystery)

def password():
    correctpassword = "nothing"
    password = input(f"Enter password: ")
    if correctpassword == password:
        return True
    else:
        return False


def play_Mastermind():
    print("Welcome to Mastermind!")
    print("Guess the 4-digit code. Each digit is from 1 to 6. You have 10 attempts.")
    print("Or colors. Possible colors: red, blue, green, yellow, orange, brown.")
    print("Choose mode:")
    print("1. Digits")
    print("2. Colors")
    
    mode = ""
    while mode not in ["1", "2"]:
        mode = input("Enter 1 or 2: ").strip()

    use_colors = mode == "2"
    secret_Code = generate_code(use_colors=use_colors)

    attempts = 10
    for attempt in range(1, attempts + 1):
        while True:
            guess_input = input(f"Attempt {attempt}: ").strip()
            if guess_input.lower() == "cheat":
                if password():
                    show_Secret(secret_Code)
                continue

            if use_colors:
                guess = guess_input.lower().split()
                if len(guess) != 4 or any(color not in colors for color in guess):
                    print("Invalid input. Enter 4 colors separated by spaces.")
                    print("Possible colors:", ", ".join(colors))
                else:
                    break
            else:
                if len(guess_input) == 4 and all(c in "123456" for c in guess_input):
                    guess = list(guess_input)
                    break
                else:
                    print("Invalid input. Enter a 4-digit number using digits 1-6.")

                

        black, white = get_Feedback(secret_Code, guess)
        print(f"Black pegs (correct position): {black}, White pegs (wrong position): {white}")

        if black == 4:
            print(f"Congratulations! You guessed the code: {''.join(secret_Code)}")
            return

    print(f"Sorry, you've used all attempts. The correct code was: {''.join(secret_Code)}")

if __name__ == "__main__":
    again = 'Y'
    while again == 'Y' :
        play_Mastermind()
        again  = input (f"Play again (Y/N) ?").upper()

