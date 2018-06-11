number = int(input('Enter number that you want to check: '))

divisors = []

for divisor in range(1, number + 1):
	if number % divisor == 0 :
		divisors.append(divisor)

print(divisors)