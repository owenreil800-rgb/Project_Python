import random
import constants_blackjack as const

STARTING_MONEY = const.CONST_STARTING_MONEY
GOAL = const.CONST_GOAL
MINIMUM_BET = const.CONST_MINIMUM_BET
TARGET = const.CONST_TARGET


def deck_of_cards():
    '''
    The definition deck_of_cards creates the deck of cards and shuffles them.

    Input:
        None

    Output: 
        shuffled deck: A list of shuffled cards]

    Side Effects:
        None
    '''
    numbers = [
                'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 
               'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 
               'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 
               'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'
               ]

    deck = [(number) for number in numbers]
    random.shuffle(deck)
    return deck


def hand_value(hand):
    '''
    This function sets the values for the face cards and the ace

    Input: 
        hand: the hand of the dealer and the player

    Output: 
        score: the value of both the player and dealers hands

    Side Effects:
        None
    '''
    
    score = 0
    aces = 0

    for number in hand:
        if number in ['J', 'Q', 'K']:
            score += 10
        elif number == "A":
            score += 11
            aces += 1
        else:
            score += int(number)

    while score > 21 and aces > 0:
        score-= 10
        aces -= 1

    return score


def show_hand(name, hand, hide_first=False):
    '''
    Shows the hand after each card is drawn for the player and the dealer

    Input: 
            name: the name of the dealer or the player
            hand: the hand of the dealer and the player
            hide_first: a boolean that hides the first card of the dealer
    
    Output: 
            The updated hands of the dealer and the player

    Side Effects:
        None
    '''
    
    if hide_first:
        cards = ["??"] + [f"{number}" for number in hand[1:]]
        print("" + "-" * 40)
        print(f"{name}: {' and '.join(cards)}")
    else:
        cards = [f"{number}" for number in hand]
        print(f"{name}: {' and '.join(cards)} for a value of {hand_value(hand)}")


def play_round(balance, bet):
    '''
    This function is the bulk of the code
    The function gives cards to the player and the dealer for their hands
    The function checks if someone wins
    The function allows the player to hit and stay
    The function then simulates the dealers hand hitting

    Input:
        balance: the amount of money the player has left
        bet: the amount of money the player bets
    
    Output: 
        balance: the updated amount of money the player has left
        result: the outcome of the round ("win", "loss", or "push")

    Side Effects:
        None
    '''

    hint = [
            "If the dealer has a 10 or an Ace showing, they have a good chance of having a blackjack.",
            "If the dealer has a 2-6 showing, they have a good chance of busting.",
            "If the dealer has a 7-9 showing, they have a good chance of winning.",
            ]
    
    deck = deck_of_cards()

    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    print(f"Your balance: ${balance:.2f}")
    print(f"Your bet: ${bet:.2f}")

    show_hand("Dealer", dealer_hand, hide_first=True)
    show_hand("You", player_hand)

    # Check for natural blackjack
    player_blackjack = hand_value(player_hand) == 21
    dealer_blackjack = hand_value(dealer_hand) == 21

    if player_blackjack or dealer_blackjack:
        show_hand("Dealer", dealer_hand)

        if player_blackjack and dealer_blackjack:
            print("Both have Blackjack! Push.")
            return balance, "push"

        if player_blackjack:
            winnings = bet * 1.5
            balance += winnings
            print("" + "-" * 40)
            print(f"Blackjack! You win ${winnings:.2f} profit!")
            return balance, "win"

        balance -= bet
        print("" + "-" * 40)
        print("Dealer has Blackjack. You lost the bet!")
        return balance, "loss"

    # Player's turn
    while hand_value(player_hand) < 21:
        choice = input("Hit or stand? (h/s): ")

        if choice == "h":
            player_hand.append(deck.pop())
            show_hand("You", player_hand)

            if hand_value(player_hand) > 21:
                balance -= bet
                print("Bust! You lost the bet!")
                print("Hint: " + random.choice(hint))
                return balance, "loss"

        elif choice == "s":
            break

        else:
            print("Enter 'h' to hit or 's' to stand.")

    # Dealer's turn
    print("Dealer's turn!")
    show_hand("Dealer", dealer_hand)

    while hand_value(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
        print("Dealer draws:")
        show_hand("Dealer", dealer_hand)

    player_total = hand_value(player_hand)
    dealer_total = hand_value(dealer_hand)

    show_hand("You", player_hand)
    show_hand("Dealer", dealer_hand)

    if dealer_total > 21:
        balance += bet
        print("" + "-" * 40)
        print(f"Dealer busts! You profit ${bet:.2f}!")
        return balance, "win"

    elif player_total > dealer_total:
        balance += bet
        print("" + "-" * 40)
        print(f"You win ${bet:.2f} profit!")
        return balance, "win"

    elif player_total < dealer_total:
        balance -= bet
        print("" + "-" * 40)
        print(f"You lost ${bet:.2f}")
        return balance, "loss"

    else:
        print("" + "-" * 40)
        print("Push! Your bet is returned.")
        return balance, "push"

def winning_statements(TARGET):
    """    
    This function contains the winning statements if the player wins

    Input:
        TARGET: a boolean that checks if the player has reached their goal of $1,000

    Output:
        statement: the final winning statement of the game if the player wins

    Side Effects:
        None
    """

    congratulations = [
            "Congratulations! You reached your goal of $1,000! Time to get the car repaired!",
            "You did it! You reached your goal of $1,000! Time to get the car repaired!",
            "Wow! You reached your goal of $1,000! Time to get the car repaired!",
            "Amazing! You reached your goal of $1,000! Time to get the car repaired!",
            "The house doesn't always win! You reached your goal of $1,000! Time to get the car repaired!"
            ]

    if TARGET==True:
        statement = random.choice(congratulations)
        return statement


def main():
    '''
    This function contains the initial statement and the final statements if the player wins or loses
    The function also checks to make sure the bets are allowed

    Input:
        None

    Output:
        Final outcome of the game, either the player wins or loses

    Side Effects:
        Target is set to True if the player reaches their goal of $1,000
    '''
    
    balance = STARTING_MONEY
    print("\n")
    print("Today is your weekly gambling trip! You have $100 in your pocket,"
            " and you really need $1,000 for your car repair.")
    print("You are all in today, so if you lose all your money, you will lose your car," 
          " but you will only leave at bankrupt or once you get the $1,000 you need!")
    print("Time for some blackjack! Good luck!")

    while 0 < balance < GOAL:
        print("\n" + "-" * 40)
        print(f"CURRENT BALANCE: ${balance:.2f}")

        max_bet = int(balance)
        if balance < MINIMUM_BET:
            print("You cannot afford to place the minimum bet.")
            break

        print(f"Bet range: ${MINIMUM_BET} to ${max_bet}")

        try:
            bet = float(input("Place your bet: $"))

            if not bet.is_integer():
                print("Please bet a whole-dollar amount.")
                continue

            bet = int(bet)

            if bet < MINIMUM_BET:
                print(f"Minimum bet is ${MINIMUM_BET}.")
                continue

            if bet > balance:
                print("You cannot bet more money than you have.")
                continue

        except ValueError:
            print("Enter a valid number.")
            continue

        balance, result = play_round(balance, bet)


    if balance >= GOAL:
        print(winning_statements(TARGET=True))
    else:
        print("" + "-" * 40)
        print("GAME OVER!")
        print("You lost all of your money! Time to say bye to your car!")

    print(f"Final balance: ${balance:.2f}")

        
if __name__ == "__main__":
    main()