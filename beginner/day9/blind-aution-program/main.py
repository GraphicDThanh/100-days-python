from replit import clear
from art import logo
# HINT: You can call clear() to clear the output in the console.
print(logo)
print("Welcome to the secret auction programming")

bidding_finished = False
bids = {}

while not bidding_finished:
  name = input("What is your name?: ")
  bid = float(input("What is your bid?: $"))
  bids[name] = bid
  should_continue = input('Are there any other bidders? Type "yes" or "no": ')
  
  if should_continue == "no":
    bidding_finished = True
  else:
    clear()

def find_the_winner(bids):
  max_bid = 0
  winner = ""
  for bid in bids:
    if bids[bid] > max_bid:
      max_bid = bids[bid]
      winner = bid

  return winner

winner = find_the_winner(bids)
print("The winner is:", winner)