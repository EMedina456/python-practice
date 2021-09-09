# Finding the medium weight out of three different weights

weight1 = int(input("Enter the first weight of the bowl: "))
weight2 = int(input("Enter the second weight of the bowl: "))
weight3 = int(input("Enter the third weight of the bowl: "))

if weight1 > weight2 and weight1 > weight3:
    if weight2 > weight3:
        print("The medium weight is " + str(weight2))
    else:
        print("The medium weight is " + str(weight3))
elif weight2 > weight1 and weight2 > weight3:
    if weight1 > weight3:
        print("The medium weight is " + str(weight1))
    else:
        print("The medium weight is " + str(weight3))
else:
    if weight1 > weight2:
        print("The medium weight is " + str(weight1))
    else:
        print("The medium weight is " + str(weight2))
