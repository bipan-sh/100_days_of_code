#Password Generator Project
import random
from random import shuffle

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

total = [letters, numbers, symbols]

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91



if nr_letters == 0 or nr_symbols == 0 or nr_numbers == 0:
    print("Password doesn't meet the criteria")

    #new_word = letters[random.randint(0, len(letters))]
else :
    new_word = letters[random.randint(0, len(letters)-1)]
    for nr_letter in range(0, nr_letters - 1) :
        new_password = letters[random.randint(0, len(numbers)-1)]
        new_word = new_word + new_password

    new_symbol = symbols[random.randint(0, len(symbols)-1)]
    for nr_symbol in range(0, nr_symbols - 1) :
        new_symbol2 = symbols[random.randint(0, (len(symbols)-1))]
        new_symbol = new_symbol + new_symbol2

    new_number = numbers[random.randint(0, len(numbers)-1)]
    for nr_number in range(0, nr_numbers - 1) :
        new_number2 = numbers[random.randint(0, (len(numbers)-1))]
        new_number = new_number + new_number2
        
    

easy_password = new_word + new_symbol + new_number
print("Your easy password is", easy_password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

list_password = list(easy_password)
random.shuffle(list_password)

hard_password = ''.join(list_password)


print(f"Your new hard password is {hard_password}")


