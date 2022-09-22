#!/usr/bin/python3

def main():
    password = []
    key = []
    username = str(input("Username: "))
    number = int(input("Number: "))
    for letter in username:
        index = ord(letter) + number
        password.append(index)
    
    for spot in password:
        i = chr(spot)
        key.append(i)
    
    key = "".join(key)
    print(key)

main()
