letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
import random
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password_chars = []   # <-- list instead of string

def add_letters():
    for _ in range(nr_letters):
        password_chars.append(random.choice(letters))

def add_symbols():
    for _ in range(nr_symbols):
        password_chars.append(random.choice(symbols))

def add_numbers():
    for _ in range(nr_numbers):
        password_chars.append(random.choice(numbers))

actions = [add_letters, add_symbols, add_numbers]

random.shuffle(actions)

for action in actions:
    action()

password = "".join(password_chars)
print(f"Your password is: {password}")




