import secrets
import string

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


def generate_password(what_is_the_password_for, num_of_numbers, num_of_special, num_of_small_letters, num_of_cap_letters):

    small_letters = string.ascii_lowercase

    Big_letters = string.ascii_uppercase

    Special_Characters = string.punctuation

    numbers = string.digits

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
    
    print(f"Password for {what_is_the_password_for}:{Password}")
    
    return Password


generate_password("facebook", num_of_numbers, num_of_special, num_of_small_letters, num_of_cap_letters)
