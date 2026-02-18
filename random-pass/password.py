from random import random, choice
from string import ascii_letters, punctuation, digits

# def genran(func):
#     def wrapper(array):
#         pass
#     return wrapper

def ranSymb(array):
    return choice(array)

def ranArray():
    pick = int((random() * 100) % 3)
    if pick == 0:
        return ascii_letters
    if pick == 1:
        return punctuation
    if pick == 2:
        return digits

def validPas(password):
    for i in password:
        if (i not in ascii_letters) and (i not in punctuation) and (i not in digits):
            return False
        return True

def missingArray(password):
    for i in password:
        if (i not in ascii_letters) and (i not in punctuation):
            return digits
        if (i not in ascii_letters) and (i not in digits):
            return punctuation
        if (i not in punctuation) and (i not in digits):
            return ascii_letters

def generatePassword(length):
    password = ""
    i = 0
    while (i < length):
        array = ranArray()
        symb = ranSymb(array)
        password += symb
        i += 1
    while not validPas(password):
        array = missingArray(password)
        symb = ranSymb(array)
        pos = int((random() * 100) % length)
        password[pos] += symb

    return password

password = generatePassword(10)
print(f"\nPassword: {password}\n")