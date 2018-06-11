import random

number = random.randint(1, 9)

user_number = int(input('Enter your guess: '))

if number < user_number :
	print('Your guess was greater than the number we had. Our number was ', number)
elif number > user_number :
	print('Your guess was less than the number we had. Our number was ', number)
else:
	print('Correct guess! Our number was ', number)