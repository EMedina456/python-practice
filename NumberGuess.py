import random

topRange = input("Type a number: ")

if topRange.isdigit():
    topRange = int(topRange)

    if topRange <= 0:
        print("Please restart and type a number larger than 0.")
        quit()

else:
    print("Please restart and type a number")
    quit()

randNum = random.randint(0, topRange)
guesses = 0

while True:
    userGuess = input("Make a guess: ")
    guesses += 1
    if userGuess.isdigit():
        userGuess = int(userGuess)
    else:
        print("Please type a number")
        continue

    if userGuess == randNum:
        print("You got it!")
        break
    elif userGuess > randNum:
        print("You were above the number. Try again!")
    else:
        print("You were below the number. Try again!")

print("It took you", guesses, "guesses")
