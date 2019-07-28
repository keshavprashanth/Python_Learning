# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.

number_string = input("Please enter a number:")
number = int(number_string)

for x in range(1, number+1):
    if number % x == 0:
        print(x, "is a divisor of", number)