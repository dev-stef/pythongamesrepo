# gives a random library for generating a random number
import random

# stores a random number within the range 1 and 50 in the variable called number
number = random.randrange(1, 50)

# gets a number guess from the user. Stores variable in guess
guess = int(input("Guess a number between 1 and 50"))

# while loop looking for the number before it will print the guessed message
while guess != number:

    # if guessed number is less than the random number then display message
    # get new guessed number
    if guess < number:
        print("Silly Human. You need to guess higher. Try Again.")
        guess = int(input("Guess a number between 1 and 50"))
    # else if guessed number is higher than the random number display message
    # get new guessed number
    elif guess > number:
        print("Nope! You need to guess lower. Try Again.")
        guess = int(input("Guess a number between 1 and 50"))
    continue
else:
    print("Victory! You guessed it human! Good Job!")
























