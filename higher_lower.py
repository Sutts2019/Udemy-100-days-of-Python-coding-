import random
from game_data import data
from art import logo, vs

print(logo)

score = 0
game_over = False
A = {}
B = {}
player = {}

def random_insta():
    choice = random.choice(data)
    return choice

def compare_followers(A, B):
    if A["follower_count"] > B["follower_count"]:
        winner = A
    else:
        winner = B
    return winner

#pick 2 random comparisons
A = random_insta()
B = random_insta()

while not game_over:
    while A == B:
        print("Identical A & B, new option B chosen")
        B = random_insta()
    print(f"Compare A: {A["name"]}, a {A["description"]} from {A["country"]}.")
    print(vs)
    print(f"Against B: {B["name"]}, a {B["description"]} from {B["country"]}.")
    player_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    if player_choice == "A":
        player = A
    elif player_choice == "B":
        player = B
    else:
        print("invalid choice, please enter 'A' or 'B'")

    print(f"You chose: {player_choice}, {player["name"]}")

    #compare A follower_count vs B follower_count, highest value
    winner = compare_followers(A,B)

    #does player choice == highest value?
    if player == winner:
        print(f"You're correct, {winner["name"]} wins with {winner["follower_count"]} million followers")
        score += 1
        A = B
        B = random_insta()
    else:
        print(f"Incorrect, {winner["name"]} had the most followers")
        print(f"Game over, you scored: {score}")
        game_over = True