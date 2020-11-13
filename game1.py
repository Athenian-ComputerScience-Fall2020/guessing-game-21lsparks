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
print("Hi! Welcome to the Guessing Game. When you want to exit, print done.")
while True:
    x = int(input("To start, decide a range. First, pick a small number.  "))
    y = int(input("Great! Now a big one.  "))
    target = random.randint(x,y)
    while True: 
        guesses = 1
        guess = input("What is your guess? ")
        if guess == "done":
            exit()
        try:
            guess = int(guess)
            if guess > target:
                print("Sorry! " +  str(guess) + " is too big!")

            elif guess < target:
                print("Sorry! " + str(guess) + " is too small.")

            else:
                print("Great job! " + str(guess) + " is correct!")
                break
        except:
            print("Whoops! That's not a number, you silly goose. Try again!")
        guesses = guesses + 1
    y = input("For a new game type Y. To exit type N. ")
    if y == "N": 
        break

print("Game over! See you next time.")