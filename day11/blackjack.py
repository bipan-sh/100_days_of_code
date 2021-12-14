
import random
from art import logo
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card():
    card = random.choice(cards)
    return card

def calculate_score(cards):
    
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if computer_score == user_score:
        print("It's a draw")
    elif computer_score == 0:
        print("Computer wins")
    elif user_score == 0:
        print("User wins")
    elif user_score > 21:
        print("Computer wins")
    elif computer_score > 21:
        print("USER wins")
    elif computer_score > user_score:
        print("Computer wins")
    elif user_score > computer_score:
        print("User wins")
    else:
        print("You lose")

def game():
    print(logo)
    user_cards = []
    computer_cards = []

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    game_over = False

 
    while game_over == False:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"user card: {user_cards}, user_score = {user_score}")
        print(f"Computer card: {computer_cards[0]} ")


        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True

        else:
            user_deal_card = input('Do you want to pull another card. Press y for yes or n for no: ')
            if user_deal_card == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    calculate_score(computer_cards)
    print(f"Your final hand: {user_cards}, your score: {user_score}")
    print(f"Computer hand: {computer_cards}, comp score: {computer_score}")
    print(compare(user_score, computer_score))

    
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  os.system('cls')
  game()
