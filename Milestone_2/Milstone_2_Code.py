password = input("Please create your password...  ")

import re

if len(password) < 15:
    print("Password short, perhaps increase the length to at least 15")

elif not re.search(r"[A-Z]", password):
    print("Password weak, perhaps add a Capital Letter!")

elif not re.search(r"[0-9]", password):
    print("Password weak, perhaps add a Number!")

elif not re.search(r"[{}/|;:',.<>?~`!@#$%^&*()]", password):
    print("Password weak, perhaps add a Special Character")

else:
    digit_sum = sum(int(digit) for digit in password if digit.isdigit())
    letter_count = sum(1 for char in password if char.isalpha())
    if digit_sum != letter_count:
        print("Password weak, perhaps all digits must add up to the number of letters in your password")
    else:
        print("Password Strong")