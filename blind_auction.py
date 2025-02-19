# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


new_bids = True
bid_list = {}

while new_bids:
    name = input("What is your name? :")
    bid = int(input("How much do you bid?:"))
    bid_list[name] = bid
    more_bidders = input("Are there any more bidders? y or n").lower()
    print("\n" * 20)
    if more_bidders != "y":
        new_bids = False

print(bid_list)
winning_bid = 0
winner = ""

for n in bid_list:
    if bid_list[n] > winning_bid:
        winning_bid = bid_list[n]
        winner = n

print(f"Winner is {winner}, with a bid of {winning_bid}.")