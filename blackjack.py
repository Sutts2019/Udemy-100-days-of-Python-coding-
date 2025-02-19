import random

def draw_card():
    random_card = random.choice(cards)
    return random_card

def score_player(player_cards):
    player_total = sum(player_cards)
    if player_total > 21 and 11 in player_cards:
        ace_index = player_cards.index(11)
        player_cards[ace_index] = 1
        player_total = sum(player_cards)
    return player_total

def score_dealer(dealer_cards):
    dealer_total = sum(dealer_cards)
    while dealer_total <17:
        computer_cards.append(draw_card())
        print("Dealer score under 17, drawing another card.")
        dealer_total = sum(dealer_cards)
        if dealer_total > 21 and 11 in computer_cards:
            ace_index = dealer_cards.index(11)
            dealer_cards[ace_index] = 1
            dealer_total = sum(dealer_cards)
    return dealer_total

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
computer_cards = []
game_over = False

print(logo)
#draw 2 cards each to start
for n in range(0,2):
    player_cards.append(draw_card())
    computer_cards.append(draw_card())

while not game_over:
    player_score = score_player(player_cards)
    print(f"Your cards: {player_cards}")
    print(f"Your score: {player_score}")
    print(f"Dealers first card: {computer_cards[0]}")

    if player_score > 21:
        print("Bust! You lose")
        break

    choice = input("Enter 'y' to draw another card, enter 'n' to stick.").lower()
    if choice == 'y':
        print("\n" * 20)
        print("You draw another card")
        player_cards.append(draw_card())
    else:
        game_over = True

dealer_score = score_dealer(computer_cards)
#print final hands and scores
print(f"Your hand: {player_cards}")
print(f"Your final score: {player_score}")
print(f"Dealers hand: {computer_cards}")
print(f"Dealers final score: {dealer_score}")

if player_score > dealer_score:
    print("You win!")
elif dealer_score > player_score:
    print("Dealer wins!")
else:
    print("Game is a draw...")