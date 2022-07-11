import os
import random
from art import logo, vs
from game_data import data

clear = lambda: os.system('cls')

#Pick a random data
def pick_random_data():
  #pick a random data 
  #but exclude in the selected list
  return random.choice(data)

#Write object sentence
def get_sentence(obj):
  return "{name}, a {desc}, from {country}.".format(
    name=obj["name"],
    desc=obj["description"],
    country=obj["country"]
  )

#Print 
def print_data(obj_a, obj_b):
  print("Compare A: ", get_sentence(obj_a))
  print(vs)
  print("Against B: ", get_sentence(obj_b))

#Check user guessing
def check_user_guess(user_guess, obj_a, obj_b):
  if obj_a["follower_count"] > obj_b["follower_count"] and user_guess == "A":
    return True
  
  if obj_a["follower_count"] < obj_b["follower_count"] and user_guess == "B":
    return True

  return False
  
def main():
  score = 0


  #Pick 2 random data A, B and print out
  obj_a = pick_random_data()
  obj_b = pick_random_data()
  
  while obj_a and obj_b:
    #Print game logo
    print(logo)
    #print data
    print_data(obj_a, obj_b)
    
    #Input user's guessing
    user_guess = input("Who has more followers? Type 'A' or 'B': ")
    
    #Check if user correct then increase score
    is_correct = check_user_guess(user_guess, obj_a, obj_b)
    
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
        obj_a = obj_b
        obj_b = pick_random_data()
    else:
        obj_a = obj_b = None
        clear
        print(f"Sorry, that's wrong. Final score: {score}")
  
main()
