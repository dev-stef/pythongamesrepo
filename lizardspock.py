from random import randint
from random import randint

# create a set list of variables
t = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

# assign a random play for the computer from list of variables
def computer_choice():
    compin = randint(0, 4)
    return compin

beats ={'rock': 'paper',
         'paper': 'scissors',
         'scissors': 'rock',
         'spock': 'lizard',
         'lizard': 'scissors'}

def user_choice():
    while True:
        user_input = input("Make a choice: {} ???".format(beats.keys()))
        if user_input in beats:
            return user_input
        if user_choice == beats[computer_choice]:
            print("{} beats {}, you win!").format(user_choice, computer_choice)
        elif computer_choice == beats[user_choice]:
            print("{} beats {}, computer wins!").format(computer_choice, user_choice)
        else:
            print("Tie.")
        print("Invalid choice.")

while again != 'no':
    (computer_choice(), user_choice())
    again = input('Would you like to play again? ')
print('Thank you for playing.')
