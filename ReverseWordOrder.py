sentence = input('Enter a sentence of your choice: ')

def reverseSentence(sentence):
	a 		= sentence.split(' ')
	reverse = ''

	for word in a:
		reverse = word + ' ' + reverse

	return reverse

	# quick way
	return ' '.join(w.split()[::-1])

print(reverseSentence(sentence))