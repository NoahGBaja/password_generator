import string
import random
from os import system

def menu():
    print("""
██████   █████  ███████ ███████  ██████  ███████ ███    ██ 
██   ██ ██   ██ ██      ██      ██       ██      ████   ██ 
██████  ███████ ███████ ███████ ██   ███ █████   ██ ██  ██ 
██      ██   ██      ██      ██ ██    ██ ██      ██  ██ ██ 
██      ██   ██ ███████ ███████  ██████  ███████ ██   ████ """)
    print("\n")

    if (isLower):
        print("● ", end="")
    else:
        print("○ ", end="")
    print("Lower Case")

    if (isUpper):
        print("● ", end="")
    else:
        print("○ ", end="")
    print("Upper Case")

    if (isDigit):
        print("● ", end="")
    else:
        print("○ ", end="")
    print("Digit")

    if (isSpecial):
        print("● ", end="")
    else:
        print("○ ", end="")
    print("Special Character")

    print("\nEnter Q to continue")

def generate():
    if (isLower):
        char_list.extend(lower)
    if (isUpper):
        char_list.extend(upper)
    if (isDigit):
        char_list.extend(digit)
    if (isSpecial):
        char_list.extend(special)
    
    password = []
    for each in range(leng):
        mix = random.choice(char_list)
        password.append(mix)
    
    password = "".join(password)
    system('cls')
    print(f"Your password is:  {password}")

lower = string.ascii_lowercase
upper = string.ascii_uppercase
digit = string.digits
special = string.punctuation + " "

isLower, isUpper, isDigit, isSpecial = False, False, False, False

char_list = []

while 1:
    while 1:
        system('cls')
        menu()
        option = str(input(">> "))
        if option == "1":
            if (isLower):
                isLower = False
            else:
                isLower = True
        elif option == "2":
            if (isUpper):
                isUpper = False
            else:
                isUpper = True
        elif option == "3":
            if (isDigit):
                isDigit = False
            else:
                isDigit = True
        elif option == "4":
            if (isSpecial):
                isSpecial = False
            else:
                isSpecial = True
        elif option.lower() == "q":
            if not isDigit and not isLower and not isUpper and not isSpecial:
                print("Please Select atleast 1 option")
                system('pause')
                continue
            else:
                break      
        else:
            print("Please Enter A Valid Input")
            system('pause')

    while 1:    
        system('cls')
        try:
            leng = int(input("Enter the password length: "))
        except ValueError:
            print("Please enter a valid input")
            system('pause')
            continue

        if leng < 8 or leng == None:
            print("that's too low!")
            system('pause')
            continue
        else:
            break
    generate()    
    repeat = str(input("Enter q to quit\n")).lower()
    if repeat == "q":
        quit()
    char_list.clear()

