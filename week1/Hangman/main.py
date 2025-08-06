import random
from art import stages,logo
from words import hangManWords

lives = 6

print(logo)

chosenWord = random.choice(hangManWords)

placeholder = ""
wordLength = len(chosenWord)
for position in range(wordLength):
    placeholder += "_"
print(placeholder)

gameOver = False
correctLetters =[]

while not gameOver:
    print(f"***************{lives}/6 LIVES LEFT***************")
    guess = input("Guess a letter:").lower()

    if guess in correctLetters:
        print(f"You have already guessed {guess}")

    display = ""

    for letter in chosenWord:
        if letter == guess:
            display += letter
            correctLetters.append(letter)
        elif letter in correctLetters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosenWord:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word you lose a life.")
        if lives == 0:
            gameOver = True
            print(f"***************IT WAS {chosenWord}!YOU LOSE.***************")

    if "_" not in display:
        gameOver = True
        print("***************YOU WIN!***************")
    print(stages[lives])