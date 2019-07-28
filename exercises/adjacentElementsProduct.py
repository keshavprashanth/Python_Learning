#Given an array of integers, find the pair of adjacent elements that has the
# largest product and return that product.

inputArray = [3, 6, -2, -5, 7, 3]
#inputArray = [5, 1, 2, 3, 1, 4]
#print(len(inputArray))
#print(len(inputArray) - 1)
#print(inputArray[0])
#print(inputArray[1])
#print(inputArray[0] * inputArray[1])

def adjacentElementsProduct(inputArray):
    for x in range(0, len(inputArray) - 1):
        product1 = inputArray[x] * inputArray[x + 1]
        if x == 0:
            final_product = product1
        else:
            final_product = max(product1, final_product)
    return final_product

print(adjacentElementsProduct(inputArray))



