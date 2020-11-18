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
#Claryse

import random
x = 0
y = 0
print("Hi! Welcome to the Guessing Game. When you want to exit, print done.")
while True:
    try:
        x = int(input("To start, decide a range. First, pick a small number.  "))
    except:
        print("Not a number. We'll use zero instead")
    try:
        y = int(input("Great! Now a big one. "))
    except:
        print("Not a number. We'll use zero instead. ")
    target = random.randint(x,y)
# This is the first part of the code. It asks the user for a range and then the random number generator makes a number in that range
    while True: 
        guesses = 1
        guess = input("What is your guess? To exit, enter done: ")
        if guess == "done":
            exit()
        # This allows the user to exit prematurely if they wish
        try:
            guess = int(guess)
            if guess > target:
                print("Sorry! " +  str(guess) + " is too big!")

            elif guess < target:
                print("Sorry! " + str(guess) + " is too small.")

            else:
                print("Great job! " + str(guess) + " is correct!")
                break
            # all of the above statements are the computers reactions to help the user reach the target number
        except:
            print("Whoops! That's not a number, you silly goose. Try again!")
        # this is to ensure that a user knows if they input a typo, and so the program doesn't break
        guesses = guesses + 1
    y = input("For a new game type Y. To exit type N. ")
    if y == "N": 
        break
# this allows the option to play again or be done
print("Game over! See you next time.")