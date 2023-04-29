import os
import platform
from art import logo



print(logo)

def clear():
    if platform.system() == 'Linux':
        os.system('clear')
    elif platform.system() == 'Windows':
        os.system('cls')

bids = {}

other_users = True

def highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
        highest_bid = bid_amount
        winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")
    

while other_users:
    name = input("What is your name?\n")
    price = int(input("What is your bid?\n$"))
    foo = input("Are there any other bidders? Type 'yes' or 'no'\n")

    bids[name] = price

    if foo == 'no':
        other_users = False
        highest_bidder(bids)
    elif foo == 'yes':
        clear()




                  
                  
