'''
Use this file to write an "open" version of the game (no test code or defined format). This will be translated into a testable program later. Use the reponse statements provided to make that transition easier.

"Your number is too high."
"Your number is too low."
"Your number is out of range."
"I'm sorry you are giving up!"
"I'm sorry, you are out of guesses."

'''
# Collaborators: 
#tutor whats his name

import random
x = int(input("Hi! To start the Guessing Game, please pick a small number.  "))
y = int(input("Great! Now a big one.  "))
target = random.randint(x,y)
print("Hi! Welcome to the Guessing Game. When you want to exit, print done.")
guesses = 1
while True:
    guess = input("What is your guess #" + str(guesses) + "? ")
    if guess == "done":
        break
    try: 
        guess = int(guess)
    except: 
        print("Whoops! That's not a number, you silly goose. Try again!")
    if guess > target:
        print("Sorry! " +  str(guess) + " is too big!")
    elif guess < target:
        print("Sorry! " + str(guess) + " is too small.")
    else:
        print("Great job! " + str(guess) + " is correct!")
        y = input("Do you want to play again? If yes, type Y ")
        if y == "N": 
            break
    guesses = guesses + 1
print("Game over! See you next time.")