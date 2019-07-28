import random

generated_number = random.randrange(1, 10)
user_input = input("Please enter a number:")
user_input_int = int(user_input)

print('Generated number is:', generated_number)
print('Your input is:', user_input_int)

if user_input_int == generated_number:
    print("Congratulations!!! You guessed right.")
else:
    if abs(generated_number - user_input_int) < 3:
        print("Your guess is close")
    else:
        print("Your guess is way too broad!!!")