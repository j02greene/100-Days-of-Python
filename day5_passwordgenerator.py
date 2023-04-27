import random
import string
print("Welcome to Password Generator\n=============================")
chars = int(input("How many characters do you want in your password? "))
special_chars = int(input("How many special characters do you want in your password? "))
numbers = int(input("How many numbers do you want in your password? "))
password = []
random_chars_list = []


for chars in range(chars):
    random_chars_list.append(str(random.choice(string.ascii_lowercase + string.ascii_uppercase )))

special_chars_list = ['!', '@', '#', '$', '%', "^", '&', '*']
numbers_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

for specialchars in range(special_chars):
    password.append(random.choice(special_chars_list))

for nums in range(numbers):
    password.append(random.choice(numbers_list))

combined = password + random_chars_list

random.shuffle(combined)

combined_string = ''.join(combined)


print(combined_string)
print(f"Your password is " + str(len(combined_string)) + " characters long.")






