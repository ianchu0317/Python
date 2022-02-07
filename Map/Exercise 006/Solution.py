# Write a Python program to convert all the characters in uppercase and lowercase and eliminate duplicate letters from a given sequence. Use map() function.

def convert(char):
	if char.isupper():
		return char.lower()
	else:
		return char.upper()


if __name__ == '__main__':
	string = "TeSTiNg"
	print("String is " + string)

	string = "".join(list(map(convert, string)))

	print("New string is : ", string)

