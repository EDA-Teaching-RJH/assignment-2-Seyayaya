### Part Four -- your code goes here. 
import random

myList = []
for x in range(1,11):
    myList.append(random.randint(1,100))

print("Here are your 10 random numbers:")
for x in myList:
    print(x)

i = 0
while i < len(myList):
    if myList[i] % 2 == 0:
        myList.pop(i)
    else:
        i += 1
print("After removing the even numbers, here are the remaining odd numbers:\n")
print(myList)


