# letter_to_number.py
import string
user_letter = input('letter: ').lower()
print(f"That letter is at {string.ascii_lowercase.index(user_letter)+1}")