import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = []
dealer_cards = []

def deal_card(user_cards, dealer_cards):
    user_cards.append(random.choice(cards))
    dealer_cards.append(random.choice(cards))

deal_card(user_cards, dealer_cards)

flag = True
while flag:
    deal_card(user_cards, dealer_cards)
    user_cards_sum = sum(user_cards)
    dealer_cards_sum = sum(dealer_cards)
    if user_cards_sum > 21:
        print("User Loses!")
    elif dealer_cards_sum > 21:
        print(f"Dealer Loses! Dealer Cards: {dealer_cards} exceeded 21.")

    print(f"Your Cards: {user_cards}. Score: {user_cards_sum}")
    print(f"Computers first card: {dealer_cards[0]}")

    if dealer_cards_sum == 21:
        print("The Dealer has a BlackJack. The Dealer wins.")
    elif user_cards_sum == 21:
        print(f"The User has a BlackJack. The User wins.\nThe Dealers cards are {dealer_cards}.")
    else:
        if 11 in user_cards and user_cards_sum > 21:
            user_cards_sum -= 10
            if user_cards_sum > 21:
                print("User Loses")
        if 11 in dealer_cards and dealer_cards_sum > 21:
            dealer_cards_sum -= 10
            if dealer_cards_sum > 21:
                print("Dealer Loses")

    user_choice = input("Type 'y' to get another card, type 'n' to pass: ")
    if user_choice == 'n':
        while dealer_cards_sum < 16:
            dealer_cards.append(random.choice(cards))
            dealer_cards_sum = sum(dealer_cards)
        if user_cards_sum < dealer_cards_sum:
            print(f"User Cards: {user_cards} and Dealers cards are {dealer_cards}. User wins!")
        elif user_cards_sum > dealer_cards_sum:
            print(f"Dealer cards: {dealer_cards}. Dealer wins!")
        flag = False





