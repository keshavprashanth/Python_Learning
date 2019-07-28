# Given a year, return the century it is in.
# The first century spans from the year 1 up to and including the year 100,
# the second - from the year 101 up to and including the year 200, etc.

def centuryFromYear(year):
    quotient_integer = (year // 100)    # // gives integer part of quotient
    quotient = year / 100

    if quotient_integer == quotient:
        return quotient_integer
    else:
        return quotient_integer + 1


print(centuryFromYear(1998))



def centuryFromYear(year):
    if 1 <= year <= 100:
        return 1
    if 101 <= year <= 200:
        return 2
    if 201 <= year <= 300:
        return 3
    if 301 <= year <= 400:
        return 4
    if 401 <= year <= 500:
        return 5
    if 501 <= year <= 600:
        return 6
    if 601 <= year <= 700:
        return 7
    if 701 <= year <= 800:
        return 8
    if 801 <= year <= 900:
        return 9
    if 901 <= year <= 1000:
        return 10
    if 1001 <= year <= 1100:
        return 11
    if 1101 <= year <= 1200:
        return 12
    if 1201 <= year <= 1300:
        return 13
    if 1301 <= year <= 1400:
        return 14
    if 1401 <= year <= 1500:
        return 15
    if 1501 <= year <= 1600:
        return 16
    if 1601 <= year <= 1700:
        return 17
    if 1701 <= year <= 1800:
        return 18
    if 1801 <= year <= 1900:
        return 19
    if 1901 <= year <= 2000:
        return 20
    if 2001 <= year <= 2100:
        return 21

print(centuryFromYear(1995))