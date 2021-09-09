# Program that finds the number of factors of any number inputted

number = int(input("Enter a number: "))
numFactors = 0
factors = []

for i in range(1, number + 1):
    if number % i == 0:
        factors.append(i)
        numFactors += 1

print("Factors: " + str(factors))
print("The number " + str(number) + " has " + str(len(factors)) + " factors.")
