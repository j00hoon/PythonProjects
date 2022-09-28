import os
from art import logo

print(logo)

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for item in auction:
    if item["bid"] > highest_bid:
      highest_bid = item["bid"]
      winner = item["name"]
  print(f"Highest bid is ${highest_bid}, and the winner is {winner}")

auction = []
bidding_finished = False

while not bidding_finished:
  tmp_auction = {}
  name = input("Name : ")
  bid = int(input("Bid : $"))
  tmp_auction["name"] = name
  tmp_auction["bid"] = bid
  auction.append(tmp_auction)

  choice = str(input("Are there other users who want to bid? yes or no\n"))
  if choice == "yes":
    os.system('clear')
  else:
    bidding_finished = True

print(auction)
find_highest_bidder(auction)

  



