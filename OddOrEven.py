number = int(input('Give me any number: '))

if (number % 2 == 0):
	print('this is an even number. It is divisible by 2')
else:
	print('this is an odd number. It is not devisible by 2')


print('-------------------- Add on 1 --------------------')

if (number % 4 == 0):
	print('The number is divisible by 4')
elif (number % 2 == 0):
	print('The number is divisible by 2')
else:
	print('The number is an odd number')


print('-------------------- Add on 2 --------------------')
num 	= int(input('Enter a number to check: '))
divide 	= int(input('Enter a number to divide by check: '))

if (num % divide == 0):
	print(num, ' is divisible by ', divide)
else:
	print('Dum! You are of no use!')