import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
dictionary_nato = {row.letter: row.code for (index, row) in data.iterrows()}


def generate_alphabet():
	word = input("Please enter a word: ").upper()
	try:
		result = [dictionary_nato[letter] for letter in word]
	except KeyError:
		print("Sorry, only letters in the alphabet and no spaces please.")
		generate_alphabet()
	else:
		print(result)


generate_alphabet()
