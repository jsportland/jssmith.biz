# number_to_letter.py
import string
user_number = int(input('Give me a number: '))
print((string.ascii_lowercase)[user_number-1])