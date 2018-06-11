length = int(input('How big fibonacci you need? '))

if (length <= 0) :
	print('Sorry!, Invalid input.')
else:
	index = 0
	series = []

	while index <= length:
		series[index] = fibonacci(index)
		index += 1

print(series)