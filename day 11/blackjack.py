import random
import clear

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"
    if user_score == computer_score:
        return "It's a draw."
    elif computer_score == 0:
        return "Lose, opponent has blackjack"
    elif user_score == 0:
        return "Win with blackjack"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "You win"
    elif computer_score > user_score:
        return "You lose"


# Hint 5: Deal the user and computer 2 cards each using deal_card() and append().

def play_game():
    print(logo)
    user_cards = []
    computer_cards = []

    for c in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # Hint 6: Create a function called calculate_score() that takes a List of cards as input
    # and returns the score.
    # Look up the sum() function to help you do this.

    is_game_over = False
    while is_game_over is False:
        user_score = calculate_score(cards=user_cards)
        computer_score = calculate_score(cards=computer_cards)
        print(f"  Your cards: {user_cards}, current score {user_score}")
        print(f"  Computer's first card: {computer_cards[0]}")

        if user_score == 0 or user_score > 21 or computer_score == 0:
            is_game_over = True
        else:

            cont = input("Do you want to draw another card? Y or N\n").lower()
            if cont == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

        while computer_score != 0 and computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(cards=computer_cards)

    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play again? (y/n): ").lower() == "y":
    clear
    play_game()