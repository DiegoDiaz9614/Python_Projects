from art import vs_banner, main_banner
from data import data_list
import random

def game():
    while True:
        subject1 = random.choice(data_list)
        subject2 = random.choice(data_list)

        answer = max([subject1, subject2], key = lambda p: p['follower_count'])
        guess = ""

        print(main_banner)
        print(f"Compare A: {subject1['name']}, {subject1['description']}, from {subject1['country']}.")
        print(vs_banner)
        print(f"Against B: {subject2['name']}, {subject2['description']}, from {subject2['country']}.")

        guess = input("Who has more followers? Type 'A' or 'B': ")

        if answer == subject1:
                correct_answer = "A"
        else:
                correct_answer = "B"

        if guess.upper() == correct_answer:
                print(f"You got it! The answer was {correct_answer}")
        else:
            print(f"Sorry, you didn't get it! The answer was {correct_answer}")
            print(main_banner)
            return
game()