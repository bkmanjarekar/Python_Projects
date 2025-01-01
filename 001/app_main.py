from art import logo, vs
from game_data import data
import os
import random


def clear_screen():
    cls = lambda: os.system('cls')
    cls()


def start_game():
    game_on = True
    score = 0
    round_win = False
    while game_on:
        clear_screen()
        print(logo)
        if round_win:
            print(f'You are right! Your current score is {score}.')

        a_idx = random.randint(0,len(data))
        b_idx = a_idx
        while data[a_idx]['follower_count'] == data[b_idx]['follower_count']:
            b_idx = random.randint(0,len(data))

        print(f"Compare A: {data[a_idx]['name']}, a {data[a_idx]['description']}, from {data[a_idx]['country']}.")
        print(vs)
        print(f"Against B: {data[b_idx]['name']}, a {data[b_idx]['description']}, from {data[b_idx]['country']}.")

        u_in = input("Who has more followers? Type 'A' or 'B' : ").upper()
        if (data[a_idx]['follower_count'] > data[b_idx]['follower_count'] and u_in == 'A') or (data[a_idx]['follower_count'] < data[b_idx]['follower_count'] and u_in == 'B'):
            score += 1
            round_win = True
        else:
            game_on = False
            clear_screen()
            print(logo)
            print(f"Sorry that's wrong. Your final score is {score}")


if __name__ == "__main__":
    start_game()
