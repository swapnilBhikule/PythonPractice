a = [5, 10, 15, 20, 25]

if (len(a) == 1):
	new_list = a
else:
	new_list = [a[0], a[len(a) - 1]]

print(new_list)