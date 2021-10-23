
import random
import stdiomask

# For randomly generated password
print("Welcome to DA PASSWORD GENERATOR")
print("Enter Password to access the generated password - ")
user_password = stdiomask.getpass()
what_is_the_password_for = input("What is the Password for? ")
print("Please enter numbers")
try:
    num_of_letters = int(
        input("How many characters should your password have: "))
except ValueError:
    num_of_letters = int(
        input("How many characters should your password have: "))
try:
    num_of_numbers = int(input("How many numbers should your password have: "))
except ValueError:
    num_of_numbers = int(input("How many numbers should your password have: "))
try:
    num_of_special = int(
        input("How many special characters should your password have: "))
except ValueError:
    num_of_special = int(
        input("How many special characters should your password have: "))
try:
    num_of_small_letters = int(
        input("How many small letters should your password have: "))
except ValueError:
    num_of_small_letters = int(
        input("How many small letters should your password have: "))
try:
    num_of_cap_letters = int(
        input("How many big letters should your password have:  "))
except ValueError:
    num_of_cap_letters = int(
        input("How many big letters should your password have:  "))

small_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']

Big_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']

Special_Characters = ['!', '@', '#', '$', '%', '^', '&', '*']

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Sp_part = ""

Num_part = ""

Small_Part = ""

Big_Part = ""
for i in range(1, num_of_numbers + 1):
    rand_num = random.choice(numbers)
    Num_part = Num_part + str(rand_num)


for i in range(1, num_of_special + 1):
    rand_sp = random.choice(Special_Characters)
    Sp_part = Sp_part + rand_sp


for i in range(1, num_of_small_letters + 1):
    rand_sm = random.choice(small_letters)
    Small_Part = Small_Part + rand_sm


for i in range(1, num_of_cap_letters + 1):
    rand_big = random.choice(Big_letters)
    Big_Part = Big_Part + rand_big


Password = Num_part + Sp_part + Small_Part + Big_Part
Access_password = input(
    "Do you want to access generated password? (Y/N): ")
if Access_password == "Y":
    ask_user_password = stdiomask.getpass()
    if ask_user_password != user_password:
        ask_user_password = stdiomask.getpass()
    else:
        print("Here is Your Password for {} : {}".format(
            what_is_the_password_for, Password))
