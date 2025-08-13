from random import randint
from art import banner

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Function to check the users guess against the answer
def check_answer(user_guess, computer_answer, turns ):
    """Checks Answer against guess, returns the number of turns remaining"""
    if user_guess > computer_answer:
        print("Too High")
        return turns - 1
    elif user_guess < computer_answer:
        print ("Too Low")
        return turns - 1
    else:
        print(f"You got it right! The answer was {computer_answer}")
        return turns
# Function to set the difficulty
def set_difficulty():
    level = input("Choose a difficulty level, easy or hard: ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    # choosing a random number between 1 and 100
    print(banner)
    print("Im thinking of a number between 1 and 100.")
    answer = randint(1,  100)

    turns = set_difficulty()
    guess = 0
    previous_guesses = set()

    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number")
        # Let the user guess a number
        guess = int(input("Make a guess:"))

        if guess in previous_guesses:
            print("You already guessed that number!")
            continue
        previous_guesses.add(guess)

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print(f"You've run out of guesses. You Lose! The number was {answer}")
            return
        elif guess != answer:
            print("Guess again!")

game()