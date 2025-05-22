#type password
password = input ("Please create your password...  ")

import re

if len(password) < 15:
 print("Password short, perhaps increase the length to atleast 15")

elif not re.search(r"[A-Z]", password):
 print("Password weak, perhaps add a Capital Letter!")

elif not re.search(r"[1234567890]", password):
 print("Password weak, perhaps add a Number!")

elif not re.search(r"[{}/|;:',.<>?~`!@#$%^&*()]", password):
 print("Password weak, perhaps add a Special Character")

elif not re.search(r"[]", password):
 print("Password weak, perhaps all digits must add up to number of letters in your password")

else:
 print("Password Strong")