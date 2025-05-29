import re



pi_digits = "3141592"
face = ["(._.)", "(*O*)", "(-_-)","(#~#)"]

while (True):

    password = input("Please create your password...  ")

    if len(password) < 8:
        print("Password short, perhaps increase the length to at least 8")

    elif not re.search(r"[A-Z]", password):
        print("Password weak, perhaps add a Capital Letter!")

    elif not re.search(r"[0-9]", password):
        print("Password weak, perhaps add a Number!")

    elif not re.search(r"[{}/|;:',.<>?~`!@#$%^&*()]", password):
        print("Password weak, perhaps add a Special Character, excluding _ - += ")

    else:
        digit_sum = sum(int(digit) for digit in password if digit.isdigit())
        letter_count = sum(1 for char in password if char.isalpha())
        symbol_count = sum(1 for c in password if not c.isalnum())

        if digit_sum != letter_count:
            print("Password weak, perhaps the sum of all the numbers must add up to the amount of letters in your password")

        elif pi_digits not in password:
            print("Password weak, perhaps contain the first 7 digits of pi in your password, ('without a dot')")

        elif not any(f in password for f in face):
            print("Password weak, perhaps contain one of these cute faces, (*o*),(._.), (-_-),(#~#)")

        elif symbol_count != (digit_sum * letter_count):
            print("Password weak, perhaps the number of special characters must be the product of the letters and sum of the numbers")

        else:
            print("Password Strong")
            break