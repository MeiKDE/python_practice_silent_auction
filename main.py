from art import logo
import os

print(logo)

bidding_finished=False
bidding_record={}

def clear():
    #Check if the system is Windows 
    if os.name=="nt": #nt means windows
        #use cls command to clear the screen
        os.system("cls")
    else: #posix means linux or mac
        #use clear command to clear the screen
        os.system("clear")

def find_highest_bidder(bidding_record):
    highest_bid=0
    highest_bidder=""
    print(f"check bidding record within for loop:, {bidding_record}")
    for bidder in bidding_record:
        bid_amount=int(bidding_record[bidder])
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            highest_bidder=bidder
    return print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")   

while not bidding_finished:
    name=input("Enter your name: ")
    price=input("Enter your bid: ")
    bidding_record[name]=price
    
    should_continue=input("Do you want to bid again? (y/n): ")
    if should_continue=='n':
        bidding_finished=True
        find_highest_bidder(bidding_record)
    elif should_continue=='y':
        clear()
    else:
        bidding_finished=False
        

