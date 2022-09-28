
import random
from Hangman_words import word_list 
from Hangman_art import logo 
from Hangman_art import stages
import os


chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)

print(f'{chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

guess_letters = []

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    os.system('clear')
    
    if guess in guess_letters:
      print("You already guessed")
    else:
      guess_letters.append(guess)

      #Check guessed letter
      for position in range(word_length):
          letter = chosen_word[position]
          #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
          if letter == guess:
              display[position] = letter
  
      #Check if user is wrong.
      if guess not in chosen_word:
        print(f"You've guess {guess}, and this is not in the chosen word.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
  
      #Join all the elements in the list and turn it into a String.
      print(f"{' '.join(display)}")
  
      #Check if user has got all letters.
      if "_" not in display:
          end_of_game = True
          print("You win.")
  
      print(stages[lives])