"""Welcome to ROULETTE SPINNER, a project developed by Francisco Cristina (https://github.com/gumballoon).
This tool simulates a roulette game where users can place bets on colors or specific numbers and track their balance.
For detailed instructions and information, please refer to the README file."""

import random

# DEFAULT DATA
black_numbers = [15, 4, 2, 17, 6, 13, 11, 8, 10, 24, 33, 20, 31, 22, 29, 28, 35, 26]
red_numbers = [32, 19, 21, 25, 34, 27, 36, 30, 23, 5, 16, 1, 14, 9, 18, 7, 12, 3]
slogans = ["It just won't stop spinning!", "Bet small, win BIG!", "Wake up. Bet. Win. Don't sleep. REPEAT!"]    # to be randomly selected and then displayed on the menu
balance = 0
balance_tracker = [0]   # keeps a record of the deposits


# TESTER FUNCTIONS
def is_number(user, print_error=False):
    """
    Checks if the user's input can be converted to an integer.
    :param user: [str] output of input()
    :param print_error: [bool] if True, it'll print a error message (default is False)
    :return: True or False
    """
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for n in user:
        if n not in numbers and print_error:
            print("That's not a valid answer...\n")
            return False
        elif n not in numbers:
            return False
    else:
        return True

def is_word(user, print_error=False):
    """
    Checks if the user's input only has characters from the alphabet
    :param user: [str] output of input()
    :param print_error: [bool] if True, it'll print a error message (default is False)
    :return: True or False
    """
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    for letter in user:
        if letter.upper() not in alphabet and print_error:
            print("That's not a valid answer...\n")
            return False
        elif letter.upper() not in alphabet:
            return False
    else:
        return True

def is_option(user, options, print_error=False):
    """
    Checks if the user's input belongs to the given options
    :param user: [str] output of input()
    :param options: [lst, tuple, dict, set] contains the valid options
    :param print_error: [bool] if True, it'll print a error message (default is False)
    :return: True or False
    """
    if user not in options and print_error:
        print("That's not a valid answer...\n")
        return False
    elif user not in options:
        return False
    else:
        return True


# MAIN FUNCTIONS
def deposit():
    """Allows the user to do a deposit and update his balance"""
    while True:
        user_deposit = input("How much do you wish to deposit? ").strip()   # .strip() will remove any accidental white-space
        if is_number(user_deposit, True):   # checks if the user's input is a number, if not it prints an error message
            user_deposit = int(user_deposit)     # converts the user's input (str) to an integer
            global balance  # the global means this variable isn't exclusive of the function, as it was assigned outside of it
            balance += user_deposit     # updates the user's balance
            balance_tracker.append(user_deposit)    # updates the record of deposits
            print(f"The deposit of {user_deposit}€ was successful. Happy betting!\n")
            break

def play():
    """Generates one round of the game, where the user can bet on the outcome of the roulette.
    It starts by processing the user's bet  - money and kind (color/number).
    It 'spins the roulette', letting the user know if we won or lost, and updating his balance.
    If the user gives any wrong input, it will inform him and take him back to the menu."""
    global balance  # the global means this variable isn't exclusive of the function, as it was assigned outside of it
    if balance == 0:
        print("Whoops, looks like you're out of money. Please do a deposit to continue.\n")
    else:
        user_bet = input("How much money do you wish to bet? ").strip()     # .strip() will remove any accidental white-space
        if is_number(user_bet, True):   # checks if the user's input is a number, if not it prints an error message
            bet = int(user_bet)     # converts the user's input (str) to an integer
            if bet > balance:
                print("Not enough balance, please make a deposit or bet less money.\n")
            else:
                print("""Choose the kind of bet you wish to do.
[C] Color [Red or Black] - Prize: 2x Bet
[N] Number [0 to 36] | Prize: 36x Bet""")
                user_kind = input("...").upper().strip()    # .upper() will match the options' format
                user_color = 0
                user_number = 0  # variables to hold the user's bet
                if is_option(user_kind, ["C", "N"], True):  # checks if the user's input is in the given options
                    if user_kind == "C":
                        print("""Please choose the color:
[R] Red
[B] Black""")
                        user_color = input("...").upper().strip()
                        if is_option(user_color, ["R", "B"], True):
                            print("Let's spin the wheel! ...", end=" ")     # end=" " will cancel the linebreak
                            user_number = False     # states that the user didn't do a number bet, to avoid future errors with if statements
                            balance -= bet      # updates the balance by subtracting the user's bet
                        else:
                            menu()
                    elif user_kind == "N":
                        user_number = input("Choose a number between 0 and 36: ").strip()
                        if is_number(user_number, True) and is_option(int(user_number), range(0, 37), True):
                            # checks if the user's input is a number and, if so, if it is in the given options
                            print("Let's spin the wheel! ...", end=" ")
                            user_number = int(user_number)
                            user_color = False  # states that the user didn't do a color bet, to avoid future errors with if statements
                            balance -= bet
                        else:
                            menu()
                else:
                    menu()  # an invalid answer to user_kind will skip to the menu

                roulette = random.randint(0, 36)  # spins the roulette, generating a random number from 0 to 36
                # checks the random number's color and prints the roulette outcome
                if roulette in red_numbers:
                    print(f"RED {roulette}")
                elif roulette in black_numbers:
                    print(f"BLACK {roulette}")
                else:
                    print("GREEN 0")

                if user_color:  # if the user bet on the color...
                        if roulette in red_numbers and user_color == "R":
                            balance += 2 * bet      # doubles the bet's value and updates the balance
                            print(f"You WON {2 * bet}€!\n")
                        elif roulette in black_numbers and user_color == "B":
                            balance += 2 * bet
                            print(f"You WON {2 * bet}€!\n")
                        else:
                            print("Bad luck! Why don't you try again?\n")
                elif user_number:    # if the user bet on the number...
                    if user_number == roulette:
                        balance += 36 * bet     # multiplies the bet by 36 and updates the balance
                        print(f"You WON {36 * bet}€!\n")
                    else:
                        print("Bad luck! Why don't you try again?\n")

def quit_menu():
    """Prints messages regarding the user's final outcome"""
    difference = balance - sum(balance_tracker)     # difference between current balance and the sum of all the user's deposits
    if difference > 0:
        print(f"Lucky you! You've made {difference}€ of profit. I'll get you next time...")
    elif difference == 0:
        print("Break even it is - no losses nor profit. A bit boring if you ask me.")
    else:
        print(f"Lucky me! You've lost {difference * -1}€. Come back anytime!")      # turns the negative value into a positive to match the sentence
    print("** Quitting now... Goodbye! **")

def menu():
    """Where the user can access all the programs functionalities, like do a deposit, play a round or simply quit the app"""
    while True:     # the user keeps coming back to the menu, until he quits (breaking the loop)
        print(f"""*** ROULETTE MADNESS ***
"{random.choice(slogans)}"
Balance: {balance}€
[D] Deposit
[P] Play
[Q] Quit""")    # prints the user's options, plus a random slogan and the user's current balance
        user_menu = input("....").upper().strip()   # .upper() matches the options format, .strip() will remove any accidental white-spac
        if is_option(user_menu, actions, True):     # checks if the user's input is in the given options
            print("")  # linebreak
            actions[user_menu]()    # calls one of the functions previously defined and stored in the dictionary "actions"
            if user_menu == "Q":
                break   # breaks the while loop
actions = {"D": deposit, "P": play, "Q": quit_menu}     # dict with all the functions that are accessed from the menu

menu()
# calls the menu function, a while loop, starting the program
