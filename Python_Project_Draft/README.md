### Overall Overview
    - To play the game, the player runs the code and reads the initial intro statement
    - The goal of the game is to go from $100 at the start to $1000
    - The state of the player is tracked by how much money they have throughout the game
        * If the player runs out of money, they lose
        * If the player gets $1000, they win
    - There is only an absolute win or an absolute loss in the game

### rules of blackjack
    The rules of the game follow the rules of blackjack:
        - Each hand the player starts with betting an eligible amount of money that they have in their balance
            * This decision is made at the beginning of each hand
            * The max gambled money value is determined by how much the player has at a given moment
        - The player and dealer compete to see who can get the closer value to 21 without going over
        - The player knows one of the dealers cards and can hit, (keep drawing cards) until they decide to stand (stop drawing cards) or they bust (have a value over 21)
        - Using the information given, the player will make the decision whether to hit or stand
        - If the player hits, then they can make the decision again, unless they bust, in which they lose the hand
        - If the player stands, then the dealers hand is revealed and they draw cards until they have a higher score than 17
        - Then the code calcualates who wins and how the players budget is affected
        - If the player wins the hand, the money they bet is multiplied by 3/2
        - Then the next hand starts
        - The loop contiues until the player either wins or loses the game

### constants_blackjack
    - This file holds all of the constants used in the other files

PROJECT_GAME FUNCTIONS:

### deck_of_cards
    - Creates a deck of cards
    - Shuffles the deck using randomness

### hand_value
    - Sets the value of the face cards equal to 10
    - Sets the values of the Ace to either 11 or 1, depending on what benefits the player/dealer

### show_hand
    - Shows the up to date hand for the player and the dealer after each card
    - The dealer's first card is initially hidden

### play_round
    - The function deals the cards to the player and the dealer
    - Then after each card following the first two each runs a while loop
    - The loop allows the player to hit until they want to stand or if they bust
    - Then there is a loop for the dealer to hit until they bust or are over a values of 17
    - The code has multiple print statements depending on the outcome of the hand

### winning_statements
    - Creates a random selection of statements that only print if the player wins
    - This code also only works if the player beats the game

### main
    - Contains the initial game storyline statement
    - Contains print statements for any invalid inputs the player uses throughout the game
    - Checks to see if the player has enough money to win
        * Allows the winning_statement code to run
    - Informs the player if they lost the game