#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
from random import randint

ANSWER_NUMBER = 0
LEVEL = 0


def make_random_number():
  return randint(0, 100)

def choose_difficulty():
  while True:
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
      return 10
    elif difficulty == "hard":
      return 5
    else:
      print("Invalid type")


def play_game(LEVEL):
    
  print(logo)
  print("Welcome to the number guessing game!")
  print("I'm thinking of a number between 1 and 100.")

  while LEVEL > 0:
    print(f"You have {LEVEL} attempts remaining to guess the number.")
    guess_number = int(input("Make a guess : "))

    if guess_number > ANSWER_NUMBER:
      print("Too high.")
    elif guess_number < ANSWER_NUMBER:
      print("Too low.")
    else:
      print("Yup! You win!")
      return
    LEVEL -= 1
  print("You lose!")
  return


  





is_game_done = False
while not is_game_done:
  ANSWER_NUMBER = make_random_number()
  print(ANSWER_NUMBER)
  
  LEVEL = choose_difficulty()
  play_game(LEVEL)

  is_continue = input("Continue? y or n : ")
  if is_continue == "y":
    continue
  elif is_continue == "n":
    is_game_done = True
  else:
    print("Invalid type")
