# Making a quiz game for python beginners
# Video link: https://www.youtube.com/watch?v=DLn3jOsNRVE
print("Welcome to my quiz!")

playing = input("Would you like to play?: ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect! Answer is 'central processing unit'.")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect! Answer is 'graphics processing unit'.")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect! Answer is 'random access memory'.")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print("Correct!")
    score += 1
else:
    print("Incorrect! Answer is 'power supply'.")

print("You got a score of " + str(score) + " out of 4!")
print("That's " + str((score / 4) * 100) + "%")
