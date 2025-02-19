import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]
computer_choice = random.randint(0,2)
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))

print(f"Computer chooses: {choices[computer_choice]}")
if player_choice >=0 and player_choice <=2:
    print(f"You chose: {choices[player_choice]}")


if player_choice < 0 or player_choice >2:
    print("You entered an invalid value, you lose!")
elif computer_choice == player_choice - 1 or player_choice == computer_choice - 2:
    print("You win")
elif player_choice == computer_choice -1 or computer_choice == player_choice -2:
    print("You lose")
elif player_choice == computer_choice:
    print("Draw")