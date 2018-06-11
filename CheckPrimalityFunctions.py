number = int(input('Enter your number to check if it\'s is prime number: '))

for item in range(2, number):
	if (number % item == 0):
		print('Sorry! Your number is not a prime number!')
		break

	if (item == number - 1):
		print('Guess what? It\'s a prime number :)')