import random

# Take two lists, write a program that returns a list that contains only the elements that are common between the lists
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = []   # Create empty list that will be used to store common values.
for x in a:
    if x in b:
        c.append(x)   # add common values found in list a and b into list c.

print(c)

# Eliminate duplicates from List.
print(sorted(c))      # Sort the list in ascending order
e = []                # Empty list to store the results
for x in range(0, len(sorted(c)) - 1):
    if sorted(c)[x] == sorted(c)[x+1]:
        continue
    else:
        e.append(sorted(c)[x])

print("list without duplicates:", e)


# Randomly generate two lists to test the above
p = list(range(random.randrange(0, 10), random.randrange(11, 100)))
q = list(range(random.randrange(0, 20), random.randrange(21, 100)))

r = []

for y in p:
    if y in q:
        r.append(y)
print(r)