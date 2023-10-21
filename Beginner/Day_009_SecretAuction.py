from Day_009_SecretAuction_resources import LOGO
import os


def add_bidder(
        bidder_name: str,
        bidder_bid: int,
        ):
    # Creates a "bidder" dictionary to add to the list of bidders
    bidder = {
        "name": bidder_name,
        "bid": bidder_bid,
    }
    list_bidders.append(bidder)


def get_highest_bidder():
    # Loops through the list of bidders, comparing the bids and extracting the
    # highest bidder
    highest_bid = 0
    highest_bidder = ""
    for idx in range(len(list_bidders)):
        if list_bidders[idx]["bid"] > highest_bid:
            highest_bid = list_bidders[idx]["bid"]
            highest_bidder = list_bidders[idx]["name"]
    print(f"The winner is {highest_bidder}, with a bid of ${highest_bid}.")


print(LOGO)
print("Welcome to the secret auction program.")
list_bidders = []
isFinished = False
while not isFinished:
    bidder_name = input("What is your name?: ")
    bidder_bid = int(input("What is your bid?: $"))
    add_bidder(bidder_name, bidder_bid)
    addingBidder = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    isFinished = addingBidder.lower() == "no"
    os.system("cls")
get_highest_bidder()
