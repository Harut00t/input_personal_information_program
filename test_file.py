import string

letter = string.digits
print(letter)

name = input("Please input a name: ")

if any(char in letter for char in name):
    print("iloveyou")