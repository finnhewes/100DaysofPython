import random
import os

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


def blackjack():
    print(logo)
    cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_cards = ['', '']
    computer_cards = ['', '']

    def deal_card():
        random_integer = random.randint(0, 13)
        return cards[random_integer]

    def opening_sequence():
        user_cards[0] = deal_card()
        user_cards[1] = deal_card()
        computer_cards[0] = deal_card()
        print(f"User's hand is: {user_cards}. (Sum of {sum(user_cards)}). Computer's hand is: {computer_cards}.")

    if input("Would you like to be dealt in? Type y or n.") == "y":
        opening_sequence()
    else:
        os.system('clear')
        blackjack()

    # opening sequence runs first, then the dealer's second card is immediately assigned, but remains hidden from user.
    computer_cards[1] = (deal_card())

    keep_playing = True
    computer_busted = False
    user_busted = False

    # player draw sequence
    user_will_draw = True
    while user_will_draw == True:
        if sum(user_cards) > 21:
            print("That's a bust, you lose!")
            user_busted = True
            user_will_draw = False
            keep_playing = False
        elif sum(user_cards) == 21:
            print("That's 21!")
            user_will_draw = False
        elif input("Would you like to hit? Type y or n.").lower() == "y":
            if deal_card == 11 and sum(user_cards) > 21:
                deal_card = 1
            user_cards.append(deal_card())
            print(f"You've reached {sum(user_cards)}.")
            print(user_cards)
        else:
            user_will_draw = False

    # computer draw sequence
    if user_busted != True:
        print(f"Computer's hand is {computer_cards}. (Sum of {sum(computer_cards)}).")
        while sum(computer_cards) < 17:
            print("Computer hits.")
            computer_will_draw = True
            while computer_will_draw == True:
                if sum(computer_cards) < 17:
                    computer_will_draw = True
                    if deal_card == 11 and sum(computer_cards) + deal_card > 21:
                        deal_card = 1
                    computer_cards.append(deal_card())
                print(computer_cards)
                if sum(computer_cards) > 21:
                    print("Computer has busted, you win!")
                    computer_busted = True
                    computer_will_draw = False
                    keep_playing = False
                else:
                    print(f"Computer has reached {sum(computer_cards)}.")
                    computer_will_draw = False
                    keep_playing = False

    # outcomes
    if sum(computer_cards) == 21:
        print("Computer has Blackjack! You lose!")
    if computer_busted == False and sum(user_cards) < sum(computer_cards) and sum(computer_cards) != 21:
        print("You lose!")
    if user_busted == False and sum(user_cards) > sum(computer_cards) and sum(computer_cards) != 21 and sum(
            user_cards) == 21:
        print("Blackjack! You win!")
    if user_busted == False and sum(user_cards) > sum(computer_cards) and sum(user_cards) != 21:
        print("You win!")
    if sum(user_cards) == sum(computer_cards) and sum(computer_cards) != 21:
        print("It's a draw!")

    # rinse and repeat
    if input("Would you like to play again? Type y or n.") == "y":
        os.system('clear')
        blackjack()


blackjack()
