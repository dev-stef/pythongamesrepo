# import from random
# from random import randint

# create a set list of variables
# t = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

# assign a random play for the computer from list of variables
# cinput = t[randint(0, 2)]

# setup player input and starting game prompt
# get = input("Rock, Paper, Scissors, Lizard, Spock?")

# beats = {'Paper':'Rock',
#          'Rock':'Scissors',
#          'Scissors':'Paper' }
# verbs = {{1: "Paper":"Covers", "Scissors": "Cuts", "Rock": "Smashes"}
#          {2:"Scissors: Decapitate", "Lizard":"Eats", "Spock":"Vaporizes"}
#          {3: "Spock": "Disproves", "Lizard":"Poisons" }}
# verb =

# set player condition to false

# while player == computer:
#    if player != computer:
#       if player: "Rock"
# else:
#    print("Curse you Human, Inconceivable! - We are tied!")


from random import randint


def getuser():
    print('Rock, Paper, Scissors, Lizard, Spock!')
    userin = input()
    if userin == 'Rock':
        userin = 0
    elif userin == 'Paper':
        userin = 1
    elif userin == 'Scissors':
        userin = 2
    elif userin == 'Lizard':
        userin = 3
    elif userin == 'Spock':
        userin = 4
    else:
        getuser()
    return userin

# beats = {'paper':'rock'
#         'rock':'scissors'
#         'scissors':'paper'
#         'lizard':'spock'
#         'lizard':'paper'
#         'paper':'spock'
#         'scissors:'lizard'          'rock':'lizard'
#         'spock':'scissors'

def getcomp():
    compin = randint(0, 4)
    return compin


def calc(user, comp):
    if user == comp:
        print("Inconceivable! - We are tied!")
    elif user == 0:
        if comp == 1:
            print("You lose - ",  comp, "smothers", user)
        else:
            print("You win -", user, "smashes", comp)
    elif user == 1:
        if comp == 2:
            print("You lose - ", comp, "slices", user)
        else:
            print("You win -", user, "smothers", comp)
    elif user == 2:
        if comp == 0:
            print("You lose - ", comp, "smashes", user)
        else:
            print("You win -", user, "slices", comp)


again = 'yes'
while again != 'no':
    calc(getuser(), getcomp())
    again = input('Would you like to play again? ')
print('Thank you for playing.')
