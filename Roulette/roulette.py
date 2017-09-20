"""CS1- Roulette Python."""

import random as r
r.seed(1)

bank_account = 1000
bet_amount = 0
bet_color = None
bet_number = None

green = [0, 37]
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]


def take_bet(color, number, amount):
    """Take in bet and assign vairbales."""
    global bet_color
    global bet_number
    global bet_amount
    bet_color = color
    bet_number = number
    bet_amount = int(amount)


def roll_ball():
    """Return a random number between 0 and 37."""
    return r.randint(0, 38)


def check_results(bet_number, bet_color):
    """Compare bet_color to color rolled.

    Compares bet_number to number_rolled.
    """
    rolled_ball = roll_ball()
    if rolled_ball in red:
        rolled_color = "Red"
    elif rolled_ball in black:
        rolled_color = "Black"
    elif rolled_ball in green:
        rolled_color = "Green"
    if rolled_color == bet_color and str(rolled_ball) == str(bet_number):
        return "Both"
    elif rolled_color == bet_color and str(rolled_ball) != str(bet_number):
        return "Color"
    else:
        return "Neither"


def payout(bet_amount, bank_account, result):
    """Return total amount won or lost by user based on results of roll."""
    winnings = 0
    print("result: " + result)
    if result == "Both":
        winnings = 35 * bet_amount
    elif result == "Color":
        winnings = 2 * bet_amount
    elif result == "Neither":
        winnings = -1 * bet_amount
    return winnings


def play_game():
    """Play the game.

    When this function is called, one full iteration of roulette,
    including:
    Take the user's bet.
    Roll the ball.
    Determine if the user won or lost.
    Pay or deduct money from the user accordingly.
    """
    color = input("What color would you like to bet on?: ")
    number = input("What number would you like to bet on?: ")
    amount = input("How much would you like to bet?: ")
    global bank_account
    take_bet(color, number, amount)
    result = check_results(bet_number, bet_color)
    winnings = payout(bet_amount, bank_account, result)
    bank_account += winnings
    if winnings > 0:
        print("Congrats! You won!")
    elif winnings < 0:
        print("Aww, you lose :(")
    print("Your new bank amount is: " + str(bank_account))
    response = input("Would you like to play again? (Y or N): ")
    if response == 'Y':
        play_game()
    elif response == 'N':
        quit()
    else:
        while(response != 'N' or response != 'Y'):
            response = input("Please enter a valid response: ")


play_game()


# Some games when loaded generate new seeds, but others do not.
# ex. save before trying to catch pokemon - same result vs different

# r.seed(5)
# print(r.randint(0, 100))

# Check result
# pay if won, or take money if lose
# FUNCTIONS SHOULD DO ONE THING ONLY - DRY Code - Don't repeat yourself
