import random
from art import logo

def dealCard():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculateScore(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        aceIndex = cards.index(11)
        cards[aceIndex] = 1
    return sum(cards)

def compare(uScore, cScore):
    if uScore == cScore:
        return "Draw"
    elif cScore == 0:
        return "YOU LOSE, OPPONENT HAS BLACKJACK"
    elif uScore == 0:
        return "YOU WON WITH A BLACKJACK"
    elif uScore > 21:
        return "YOU WENT OVER, YOU LOSE"
    elif cScore > 21:
        return "OPPONENT WENT OVER, YOU WIN"
    elif uScore > cScore:
        return "YOU WIN!"
    else:
        return "YOU LOSE!"
def playGame():
    print(logo)
    userCards = []
    computerCards = []
    computerScore = -1
    userScore = -1
    isGameOver = False

    for _ in range(2):
        userCards.append(dealCard())
        computerCards.append(dealCard())

    while not isGameOver:
        userScore = calculateScore(userCards)
        computerScore = calculateScore(computerCards)
        print(f"Your cards: {userCards}, current score: {userScore}")
        print(f"Computer's first card: {computerCards[0]} ")

        if userScore == 0 or computerScore == 0 or userScore > 21:
            isGameOver = True
        else:
            userShouldHit = input("Type 'y' to hit, or type 'n' to pass:")
            if userShouldHit == 'y':
                userCards.append(dealCard())
            else:
                isGameOver = True

    while computerScore != 0 and computerScore < 17:
        computerCards.append(dealCard())
        computerScore = calculateScore(computerCards)

    print(f"Your final hand: {userCards}, final score: {userScore}")
    print(f"Computer's final hand: {computerCards}, final score: {computerScore}")
    print(compare(userScore, computerScore))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n':") == "y":
    print("\n" * 20)
    playGame()