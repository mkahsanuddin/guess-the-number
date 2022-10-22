#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from art import logo

print(logo)

print("""Welcome to the Number Guessing Game!
I'm thinking of a number between 1 to 100.""")

computer_thinking = random.randint(1, 100)
print(f"Pssst, the correct answer is {computer_thinking}")

choose_difficulty = input(
    "Choose a difficulty. Type 'easy' or 'hard': ").lower()

easy_attempt = 10
hard_attempt = 5


def game():
    if choose_difficulty == "easy":
        global easy_attempt
        print(
            f"You have {easy_attempt} attempts remaining to guess the number.")
        game_end = False
        while not game_end:
            easy_attempt -= 1

            guess = int(input("Make a guess: "))
            if guess < computer_thinking and easy_attempt != 0:
                print("Too low.")
                print("Guess again.")
                print(
                    f"You have {easy_attempt} attempts remaining to guess the number."
                )
            elif guess > computer_thinking and easy_attempt != 0:
                print("Too high.")
                print("Guess again.")
                print(
                    f"You have {easy_attempt} attempts remaining to guess the number."
                )

            elif guess == computer_thinking:
                print(f"You got it! The answer was {computer_thinking}")
                game_end = True

            if easy_attempt == 0:
                print("You've run out of guesses, you lose.")
                game_end = True

    elif choose_difficulty != "easy":
        global hard_attempt
        print(
            f"You have {hard_attempt} attempts remaining to guess the number.")
        game_end = False
        while not game_end:
            hard_attempt -= 1

            guess = int(input("Make a guess: "))
            if guess < computer_thinking and hard_attempt != 0:
                print("Too low.")
                print("Guess again.")
                print(
                    f"You have {hard_attempt} attempts remaining to guess the number."
                )
            elif guess > computer_thinking and hard_attempt != 0:
                print("Too high.")
                print("Guess again.")
                print(
                    f"You have {hard_attempt} attempts remaining to guess the number."
                )

            elif guess == computer_thinking:
                print(f"You got it! The answer was {computer_thinking}")
                game_end = True

            if hard_attempt == 0:
                print("You've run out of guesses, you lose.")
                game_end = True


game()
