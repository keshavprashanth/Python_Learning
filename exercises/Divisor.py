num = input("Enter a number")
num = int(num)
listnum = list(range(1, num))
for ele in listnum:
    if num % ele == 0:
        print(ele)

