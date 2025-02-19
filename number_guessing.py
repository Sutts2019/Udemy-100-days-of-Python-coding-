import random

def choose_difficulty():
    choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if choice == "easy":
        level = 10
    elif choice == "hard":
        level = 5
    else:
        print("Invalid option")
        choose_difficulty()
    return level


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
random_number = random.randint(1,100)

attempts = (choose_difficulty())
print(f"attempts = {attempts}")

while attempts > 0:
    print(f"You have {attempts} attempts left to guess the correct number")
    guess = int(input("Make a guess: "))
    attempts -= 1
    if guess == random_number:
        print("Correct!")
        attempts = 0
    elif guess > random_number:
        print("Too high!")
        if attempts == 0:
            print(f"You have run out of guesses. I was thinking of {random_number}")
    elif guess < random_number:
        print("Too low")
        if attempts == 0:
            print(f"You have run out of guesses. I was thinking of {random_number}")

print("Game Over")