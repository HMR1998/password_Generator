import random
import string

letter = string.ascii_letters
print(letter)

numbers = string.digits
print(numbers)

symbols = "!@#%^&8()"
print(symbols)

letters_in_pw = int(input("How many letter would you like?"))
print(letters_in_pw)

symbols_in_pw = int(input("How many symbols would you like?"))
print(symbols_in_pw)

number_in_pw = int(input("How many number would you like"))
print(number_in_pw)

password = []
str_password = ""

for i in range(letters_in_pw):
    password.append(random.choice(letter))

for i in range(symbols_in_pw):
    password.append(random.choice(symbols))

for i in range(number_in_pw):
    password.append(random.choice(numbers))

random.shuffle(password)
for i in password:
    str_password += i
print(str_password)
