#Number Guessing Game Objectives:
import random
from art import logo

def game_guess_number(attempts):
  is_finish = False
  while not is_finish:
    if attempts == 0:
      is_finish = True
      print(f"Out of attempts. You lose. The number is {number}")
    else:
      guess_number = int(input("Make a guess: "))
      if guess_number == number:
        print(f"You got it! The answer was {number}.")
        is_finish = True
      else:
        if guess_number < number:
          print("Too low")
        else:
          print("Too high")
    
        attempts -= 1
        print("Guess again.")
        print(f"You have {attempts} attempts remaining to guess the number.")
        is_finish = False

# Include an ASCII art logo.
print(logo)
print("Welcome to the Number Guessing Game!")
# Allow the player to submit a guess for a number between 1 and 100.
print("I'm thinking of a number between 1 and 100.")
number = random.choice(range(100))
attempts = None
game_level =  input("Choose a difficulty. Type 'easy' or 'hard': ")
if game_level == "easy":
  attempts = 10
elif game_level == "hard":
  attempts = 5
else: 
  print("Not support this level")

if attempts:
  print(f'You have {attempts} attempts remaining to guess the number.')
  game_guess_number(attempts)

# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

