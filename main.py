# ANCHOR: IMPORTS
import secrets
import pwinput
from cryptography.fernet import Fernet
import os

# FIXME: cryptography.fernet.InvalidToken
# Solution: store key in a file then access it as everytime the program runs the key is newly generated so it cannot access previous passwords.
#Problem: how to store the key securely if stored in plain text then it is a problem!

def access_password(context, key):
    if os.path.isfile(f'{context}_password.txt'):
        print("File Exists Retreiving the password....")
        with open(f'{context}_password.txt', 'r', encoding='base64') as f:
            password_in_file = f.readlines()
        fernet = Fernet(key)
        return fernet.decrypt(password_in_file)
    else:
        print("The File with the password does not exist.")

def authenticate(password, key):
    if os.path.isfile('userPassword.txt'):
        with open('userPassword.txt', 'r', encoding='utf-8') as f:
            password_in_file = f.readlines()
        fernet = Fernet(key)
        password_in_str = ''.join(password_in_file)
        password_in_bytes = bytes(password_in_str, encoding='utf-8')
        if password == fernet.decrypt(password_in_bytes):
            print("Authentication successful!")
            return True
        
    else:
        print("You have no password. or you have deleted the file in which the file was stored in.")
        return False
    


# ANCHOR: Function for generating password
def generate_password(what_is_the_password_for):
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

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    Sp_part = ""

    Num_part = ""

    Small_Part = ""

    Big_Part = ""
    
    # ANCHOR: Generating Password
    for i in range(1, num_of_numbers + 1):
        rand_num = secrets.choice(numbers)
        Num_part = Num_part + str(rand_num)


    for i in range(1, num_of_special + 1):
        rand_sp = secrets.choice(Special_Characters)
        Sp_part = Sp_part + rand_sp


    for i in range(1, num_of_small_letters + 1):
        rand_sm = secrets.choice(small_letters)
        Small_Part = Small_Part + rand_sm


    for i in range(1, num_of_cap_letters + 1):
        rand_big = secrets.choice(Big_letters)
        Big_Part = Big_Part + rand_big


    Password = Num_part + Sp_part + Small_Part + Big_Part
    encrypted_generated_password = fernet.encrypt(bytes(Password, encoding='utf-8'))

    try:
        with open(f"{what_is_the_password_for}_password.txt",'w',encoding = 'utf-8') as f:
            f.write(f"{what_is_the_password_for}: {encrypted_generated_password}")
    finally:
        f.close()


print("Welcome to DA PASSWORD GENERATOR")
key = Fernet.generate_key()
fernet = Fernet(key)
while True:
    what_the_user_wants = input("Do you want to access previously generated passwords?(Y/N)\n")
    if what_the_user_wants != 'Y' and what_the_user_wants != 'N':
        what_the_user_wants = input("Do you want to access previously generated passwords?(Y/N)\n")
    else:
        break


if what_the_user_wants == 'N':
    print("Enter Your Password: (This will be asked from you later when you will have to enter the password, to acces the passwords)")

    user_password = pwinput.pwinput(mask='X')

    what_is_the_password_for = input("What is the Password for? ")
    print("Please enter numbers.")


    encrypted_password = fernet.encrypt(bytes(user_password, encoding='utf8'))

    try:
        with open("userPassword.txt",'w',encoding = 'utf-8') as f:
         f.write(f"{encrypted_password}")
    finally:
        f.close()

    generate_password(what_is_the_password_for)
elif what_the_user_wants == 'Y':
    password_input = pwinput.pwinput(mask='X')
    if authenticate(password_input, key):
        which_password_user_wants = input("Which Password do you want?: \n")
        password_which_user_wants = access_password(what_the_user_wants, key)
        print(password_which_user_wants)
