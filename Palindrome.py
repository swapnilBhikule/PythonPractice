str = input('Enter any string: ')

str_len = len(str) - 1

index = 0
while index <= str_len:
	if str[index] != str[str_len - index] :
		print('String is not a palindrome!')
		break

	index += 1