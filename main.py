import secrets
import random
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


def generate_password( num_of_numbers, num_of_special, num_of_small_letters, num_of_cap_letters):

    smallLetters = list(string.ascii_lowercase)

    bigLetters = list(string.ascii_uppercase)

    specialCharacters = list(string.punctuation)

    numbers = list(string.digits)

    spPart = ""

    numPart = ""

    smallPart = ""

    bigPart = ""
    
    # ANCHOR: Generating Password
    for i in range(1, num_of_numbers + 1):
        randNum = secrets.choice(numbers)
        numPart = numPart + str(randNum)


    for i in range(1, num_of_special + 1):
        randSp = secrets.choice(specialCharacters)
        spPart = spPart + randSp


    for i in range(1, num_of_small_letters + 1):
        randSm = secrets.choice(smallLetters)
        smallPart = smallPart + randSm


    for i in range(1, num_of_cap_letters + 1):
        randBig = secrets.choice(bigLetters)
        bigPart = bigPart + randBig

    password = list(numPart + spPart + smallPart + bigPart)
    random.shuffle(password)
    password_str = ''.join(password)
    
    return password_str


password = generate_password( num_of_numbers, num_of_special, num_of_small_letters, num_of_cap_letters)

print(f"Password for facebook {password}")
