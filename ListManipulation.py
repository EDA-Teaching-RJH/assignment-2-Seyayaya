### Part Three -- your code goes here. 

myList = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
orderedList = sorted(myList)
newList = []
for x in orderedList:
    if x != 1:
        newList.append(x)
newList.append(7)
newList.append(8)
print(newList)