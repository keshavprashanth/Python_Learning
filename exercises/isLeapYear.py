# 3 criteria must be taken into account to identify leap years:
# The year is evenly divisible by 4;
# If the year can be evenly divided by 100, it is NOT a leap year, unless;
# The year is also evenly divisible by 400. Then it is a leap year.
# Write a function that takes a year as a parameter and returns True if the year is a leap year, False otherwise


def isLeapYear(year):
    if year % 100 == 0 and year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


print(isLeapYear(2019))
