password = input("Please create your password...  ")
#import re for re.search later
import re
#pie digits for later
pi_digits = "3141592"

face = "(._.)","(*O*)","(-_-)"

if len(password) < 8:
    print("Password short, perhaps increase the length to at least 8")

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

    elif pi_digits not in password:
        print("Password weak, perhaps contain the first 7 digits of pie in your password")
    
    elif face not in password:
        print("Password weak, perhaps contain one of these cute faces, (*O*),(._.), (-_-)")

    else:
        print("Password Strong")