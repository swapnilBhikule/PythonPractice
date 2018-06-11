a = [1, 1, 2, 2, 3, 4, 4, 34, 35, 77, 77, 78, 87, 89, 100]

def unique(a):
	unique_a = []
	for item in a:
		if item not in unique_a:
			unique_a.append(item)

	return unique_a

print(unique(a))