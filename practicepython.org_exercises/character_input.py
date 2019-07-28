import datetime
# Program to take name and age as user input and display the year when they will turn 100 year old.

name = input("Please enter your name:")
age_string = input("Please enter your age:")

age_int = int(age_string)
current_date = datetime.datetime.now()
current_year = current_date.year

years_100 = current_year + (100 - age_int)

print("Hello", name, "You will turn 100 years old in the year:", years_100)
