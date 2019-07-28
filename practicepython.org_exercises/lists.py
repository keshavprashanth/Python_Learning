a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for x in a:
    if x < 5:
        print(x)
#       print(x, end=" ")  # print in one line

b = []

for y in a:
    if y < 5:
        b.append(y)

print(b)