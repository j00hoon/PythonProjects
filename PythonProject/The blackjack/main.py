############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

from art import logo
import os
import random




def play_game():
  final_result = ""
  user_card = []
  com_card = []

  for i in range(2):
    user_card.append(deal_card())
    com_card.append(deal_card())

    
  is_game_over = False
  while not is_game_over:
    user_card_score = calculate_score(user_card)
    com_card_score = calculate_score(com_card)
    
    print("User card : ", user_card)
    print("Com card : ", com_card[0])

    user_win_blackjack = False
    com_win_blackjack = False
    if user_card_score == 0:
      user_win_blackjack = True
    if com_card_score == 0:
      com_win_blackjack = True
      
    if user_win_blackjack or com_win_blackjack:
      if com_win_blackjack:
        final_result = "You lose, com blackjack"
      elif user_win_blackjack:
        final_result = "You win, you blackjack"
      

    keep_going = str(input("Type 'y' to get another card, type 'n' to pass: "))
    if keep_going == "y":
      user_card.append(deal_card())
    else:
      is_game_over = True

  while com_card_score != 0 and com_card_score < 17:
    com_card.append(deal_card())
    com_card_score = calculate_score(com_card)

  final_result = compare(user_card_score, com_card_score)


  print(f"User card : {user_card}")
  print(f"Com card : {com_card}")
  print(f"Final result : {final_result}")
  print(f"User score : {user_card_score}")
  print(f"Com score : {com_card_score}")




def compare(user_score, computer_score): 
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"


  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"




def calculate_score(card):
  card_sum = sum(card)
  if card_sum == 21 and len(card) == 2:
    return 0
  elif card_sum > 21 and 11 in card:
    card.remove(11)
    card.append(1)

  return sum(card)
  
  

  

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)

  



while input("Do you want to play a game of Blackjack? Type 'y' or 'n' ") == "y":
  os.system("clear")  
  print(logo)
  play_game()