'''
Use this file to write an "open" version of the game (no test code or defined format). This will be translated into a testable program later. Use the reponse statements provided to make that transition easier.

"Your number is too high."
"Your number is too low."
"Your number is out of range."
"I'm sorry you are giving up!"
"I'm sorry, you are out of guesses."

'''
# Collaborators: 


import random
target = random.randint(0,10)
print(target)
print("Hi! Welcome to the Guessing Game. You have five guesses.")
for guesses in range(1, 6):
    guess = input("What is your guess #" + str(guesses) + "? ")
    if guess == "done":
        exit()
    guess = int(guess)
    if guess > target:
        print("Sorry! " +  str(guess) + " is too big!")
    elif guess < target:
        print("Sorry! " + str(guess) " is too small")
    else:
        print("Great job! " + str(guess) + " is correct!")
        exit()
