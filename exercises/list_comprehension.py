# Print ages in a new list using list comprehension
years_of_birth = [1990, 1991, 1990, 1990, 1992, 1991]
ages = [2014 - year for year in years_of_birth]

print(ages)

# Print even numbers in a new list using list comprehension
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
even = [x for x in a if x % 2 == 0]
print(even)

# Create a list of squares using list comprehension
squares = [x**2 for x in range(10)]
print(squares)

# We can have multiple for loops and if conditions.
pairs = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(pairs)


p=q=r=2
n=3
list = [[p, q, r] for p in range(x+1) for q in range(y+1) for r in range(z+1) if p+q+r != n]
print(list)
