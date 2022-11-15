from art import logo
from art import vs
from game_data import data
from random import randint
import os



score = 0


def play_game():
    global score
    compare_a = choose_from_data()
    compare_b = choose_from_data()

    if compare_a == compare_b:
        compare_b = choose_from_data

    print(f"Compare A : {format_data(compare_a)}.")
    print(vs)
    print(f"Compare B : {format_data(compare_b)}.")

    choice = str(input("Who has more followers? 'A' or 'B': "))
    if compare_A_B(compare_a, compare_b) == choice:
        score += 1
        print(f"You're right! Current score : {score} ")
        return True
    else:
        return False


def format_data(compare_data):
    return f"{compare_data['name']}, {compare_data['description']}, {compare_data['country']}"



def compare_A_B(compare_a, compare_b):
    follower_a_cnt = int(compare_a['follower_count'])
    follower_b_cnt = int(compare_b['follower_count'])

    if follower_a_cnt > follower_b_cnt:
        return 'A'
    elif follower_a_cnt < follower_b_cnt:
        return 'B'


def choose_from_data():
    return data[randint(0, len(data) - 1)]







is_game_over = False



while not is_game_over:
    print(logo)
    result = play_game()
    if not result:
        print(f"Sorry, that's wrong. Final score: {score}")
        is_game_over = True
        choice = str(input("Continue? 'y' or 'n' : "))
        if choice == 'n':
            break
    os.system("clear")  
    is_game_over = False
    score = 0

