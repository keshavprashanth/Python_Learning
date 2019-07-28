def checkout():
    total = 0
    count = 0
    moreItems = True

    while moreItems:
        price = float(input("Enter price of item (Enter 0 when done):"))
        if price != 0:
            total = total + price
            count = count + 1
            print("Subtotal:", price)
        else:
            moreItems = False

    average = total / count
    print("Total items:", count)
    print("Total $:", total)
    print("Average price per item: $", average)


checkout()
