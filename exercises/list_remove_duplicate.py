myList = [1, 2, 3, 1, 2, 5, 6, 7, 8]
cleanlist = []

[cleanlist.append(x) for x in myList if x not in cleanlist]

#2nd option
cleanlist2=[]
for x in myList:
    if x not in cleanlist2:
        cleanlist2.remove(x)
print(cleanlist2)

