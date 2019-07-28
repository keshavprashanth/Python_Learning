#Ratiorg got statues of different sizes as a present from CodeMaster for his birthday,
# each statue having an non-negative integer size. Since he likes to make things perfect,
# he wants to arrange them from smallest to largest so that each statue will be bigger than
# the previous one exactly by 1. He may need some additional statues to be able to accomplish that.
# Help him figure out the minimum number of additional statues needed.

statues = [6, 2, 3, 8]

def makeArrayConsecutive2(statues):
    statues.sort()
    total = 0
    for x in range(0, len(statues) - 1):
        if statues[x+1] - statues[x] == 1:
            continue
        else:
            total = total + ((statues[x+1] - statues[x]) - 1)
    return total

print(makeArrayConsecutive2(statues))