import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# EASY LEVEl

# password = ""
# for char in range(1, nr_letters + 1):
#     password += random.choice(letters)
#
# for char in range(1, nr_symbols + 1):
#     password += random.choice(symbols)
#
# for char in range (1, nr_numbers + 1):
#     password += random.choice(numbers)
# password.split()
# print(password)


# /HARD LEVEL
r1 = random.choices(letters, k= nr_letters)
r2 = random.choices(numbers, k=nr_numbers)
r3 = random.choices(symbols, k= nr_symbols)
combined = []
for c in r1:
    combined.append(c)
for c in r2:
    combined.append(c)
for c in r3:
    combined.append(c)
print(combined)
random.shuffle(combined)
print(combined)
password = ""
for q in combined:
    password += q
print(f"Your password is {password}")


