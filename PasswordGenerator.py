import string
import random

size = int(input('How long your password must be? '))
strongness = int(input('How strong your password must be? (0: low | 1: medium | 2: high): '))

def pwdGenerator(size, strongness):
	chars = string.ascii_letters

	if strongness == 1 :
		chars += string.digits
	elif strongness == 2 :
		chars += string.punctuation

	return ''.join(random.choice(chars) for count in range(size))


print(pwdGenerator(size, strongness))