import random
from art import logo

def deal_card():
    cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(player_cards_):
    score = sum(player_cards_) 
    if sum(player_cards_) == 21 and len(player_cards_)  == 2:
        score = 0
        return player_cards_, score

    if 11 in player_cards_ and score > 21:
        player_cards_.remove(11)
        player_cards_.append(1)
        print(f"Ace card!, Deck: {player_cards_}")
        score = sum(player_cards_)
    return player_cards_, score

def who_win(your_score_, computer_score_):
    if your_score_ == computer_score_ :
        print(f"It's a draw. You have {your_score_} and Computer has {computer_score_}")
    elif your_score_ == 0:
        print(f"Wowww!! You win with a Blackjack!!!")
    elif computer_score_ == 0:
        print(f"Lose, opponent has a Blackjack!!!")
    elif your_score_ > 21:
        print(f"You lose. You went over. Your score is {your_score_}")
    elif computer_score_ > 21:
        print("Oponent went over. You win")
    elif your_score_ <= 21 and your_score_ > computer_score_:
        print(f"Congrats!!! You win! You has {your_score_} and opponent has {computer_score_}")
    else: 
        print(f"You lose. You has {your_score_} and opponent has {computer_score_}")

def game():
    your_cards = []
    computer_cards = []
    choice = input("\nDo you want to play a Blackjack? Tipe 'y' or 'n': ").lower()
    print(logo)
    
    if choice == 'y':
        for _ in range(2):
            your_cards.append(deal_card())
            computer_cards.append(deal_card())

    while choice == "y":
        computer_cards, computer_score = calculate_score(computer_cards)
        your_cards, your_score = calculate_score(your_cards)
        print(f"\nYour cards: {your_cards}, current score: {your_score}")

        while computer_score != 0 and computer_score < 18:
            computer_cards.append(deal_card())
            computer_cards, computer_score = calculate_score(computer_cards)

        if your_score == 0 or your_score >= 21 or computer_score == 0:
            who_win(your_score, computer_score)
            choice = "n"
        else:
            choice = input("\nType 'y' to get another card, type 'n' to pass: ").lower()
            if choice == "y":
                your_cards.append(deal_card())
            else:
                who_win(your_score, computer_score)
    game()
game()
