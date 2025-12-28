# This is day 6 of my internship

"""
Task:
Write a program to guesse the number between 1 - 100, show greater than or lower than according to the number.
"""
import random

answer = round((random.random() * 100) + 1, None)
rounds = 1
max_rounds = 6
running = True

print("Guess the number between 1 to 100.")
print("--------------------------------------")

while running:

    user_input = int(input("Guess the number: "))

    if user_input == answer:
        print(
            f"You guessed the correct answer in {rounds} rounds. The correct number is: {answer}"
        )
        running = False

    elif answer > user_input:
        print(f"{user_input} is less than the Number. Remaining rounds {max_rounds - rounds}")
        rounds += 1
        print("--------------------------------------")

    elif answer < user_input:
        print(f"{user_input} is greater than the Number. Remaining rounds {max_rounds - rounds}")
        rounds += 1
        print("--------------------------------------")

    else:
        print(f"Please enter a valid number. Remaining rounds {max_rounds - rounds}")
        rounds += 1
        print("--------------------------------------")

    if rounds == max_rounds:
        print(f"You are out of the number of guesses. The correct answer is: {answer}. Remaining rounds are: {rounds - max_rounds}")
        running = False
        print("--------------------------------------")
