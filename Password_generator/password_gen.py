import random
import string

characters = string.ascii_letters + string.punctuation + string.digits
char_count = (int(input("How many characters?: ")))

password = ""
for i in range(char_count):
    password += random.choice(characters)


print(password)