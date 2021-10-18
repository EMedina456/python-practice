# Determine whether a given person is old enough to vote
import re

f = open("votes.txt", "r")
numVotes = int(f.readline())

for i in range(0, numVotes):
    birthday = f.readline()
    year, month, day = re.split(' |-', birthday)
    if int(year) < (2007 - 18):
        print("Yes")
    elif int(year) == (2007 - 18):
        if int(month) < 2:
            print("Yes")
        elif int(month) == 2:
            if int(day) <= 27:
                print("Yes")
            else:
                print("No")
        else:
            print("No")
    else:
        print("No")
