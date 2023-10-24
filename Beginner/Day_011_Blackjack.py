from Day_011_Blackjack_resources import LOGO, DECK
import random
import os


def draw_card(deck: list[int]) -> int:
    """Draws a card at random from the available cards."""
    return random.choice(deck)


def obtain_score(cards):
    """Return the score from a given list of cards using blackjack rules."""
    score = sum(cards)
    # Checks for blackjack
    if len(cards) == 2 and score == 21:
        return 0
    # Converts all aces into ones if above 21
    while score > 21 and 11 in cards:
        cards[cards.index(11)] = 1
        score = sum(cards)
    return score


def compare_scores(player_score, dealer_score):
    if player_score > 21:
        playerBusted()
    elif dealer_score > 21 or (dealer_score < player_score and dealer_score != 0):
        playerWins()
    elif dealer_score == player_score:
        playerDraw()
    elif player_score == 0:
        playerBlackjack()
    else:
        playerLoses()


def playerBlackjack():
    print("Blackjack!!!")
    print("That was quite some luck!")


def playerBusted():
    print("You busted...")
    print("Better luck next time!")


def playerDraw():
    print("Draw! That was close...")
    print("Better luck next time!")


def playerLoses():
    print("You lost...")
    print("Better luck next time!")


def playerWins():
    print("Congratulations, you won!")


def main():
    starting = input("Do you want to play a game of Blackjack? Type 'y' to play a game, else type 'n': ")
    isRunning = starting == 'y'
    while isRunning:
        # Clears the screen
        os.system("cls")
        # Initialization
        print(LOGO)
        dealer_hand = []
        player_hand = []
        deck = DECK
        # The dealer draws the first card
        dealer_hand.append(draw_card(deck))
        dealer_hand.append(draw_card(deck))
        dealer_score = obtain_score(dealer_hand)
        print(f"Dealer's hand: [{dealer_hand[0]}, ?] - Score: ?")
        # The player draws the first card
        player_hand.append(draw_card(deck))
        # Loop for the player to draw subsequent cards
        playerIsDrawing = True
        playerHasBusted = False
        while playerIsDrawing:
            player_hand.append(draw_card(deck))
            player_score = obtain_score(player_hand)
            print(f"Player's hand: {player_hand} - Score:", player_score)
            if player_score > 21:
                # Player has busted
                # NOTE: currently it just skips the draw of the dealer
                playerHasBusted = True
                playerIsDrawing = False
            elif player_score == 21 or player_score == 0:
                # Player did 21, no reason to draw more cards
                playerIsDrawing = False
            else:
                # Ask the player if they want to draw more cards
                drawing = input("Do you want to draw another card? Type 'y' to draw, 'n' to pass the turn: ")
                playerIsDrawing = drawing == 'y'
        # The dealer draws cards until its score is above 16
        while not playerHasBusted and dealer_score < 17 and dealer_score != 0:
            dealer_hand.append(draw_card(deck))
            dealer_score = obtain_score(dealer_hand)
        # Shows final situation
        print("-------------------------------")
        print(f"Your hand: {player_hand} - Score: {player_score}")
        print(f"Dealer's hand: {dealer_hand} - Score: {dealer_score}")
        print("-------------------------------")
        # Evaluates the scores
        compare_scores(player_score, dealer_score)
        replay_answer = input("Do you want to play another match? Type 'y' or 'n': ")
        isRunning = replay_answer == 'y'
    print("Goodbye!")


if __name__ == '__main__':
    main()