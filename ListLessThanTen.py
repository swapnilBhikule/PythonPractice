a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for item in a:
	if (item < 5):
		print(item, ' is less than 5')

print('-------------------- Add on 1 --------------------')
less = []

for item in a:
	if (item < 5):
		less.append(item)

print(less)


print('-------------------- Add on 3 --------------------')
num = int(input('Enter any number: '))
smaller = []

for item in a:
	if item < num:
		smaller.append(item)

print(smaller)