import os 
from os import system 
from colorama import Fore, Back, Style

system('clear')

isNotZero = False

# -- Functions ------
def add(num1, num2):
    addCalculate = num1 + num2
#   addCalculate = 2 + 3
    return addCalculate 
#   return 5

def subtract(num1, num2):
    subtractCalculate = num1 - num2
    return subtractCalculate

def multiply(num1, num2):
    multiplyCalculate = num1 * num2 
    return multiplyCalculate

def divide(num1, num2):
    if (num2 == 0):
        try:
            divideCalculate = num1 / num2
        except ZeroDivisionError: print(f'Not possible division by {n2}')
    else:
        divideCalculate = num1 / num2
        return divideCalculate

def printModulus(num1, num2):
    modulusCalculate = num1 % num2
    return modulusCalculate

def printName(n):
    print(Fore.CYAN, 'Cool! Your name is {}'.format(n))

def displayPersonalInfo(firstName, lastName, age, phone):
    print(Fore.GREEN, f'''
        This is the data that we collected from you:
        First Name:...........{firstName}
        Last Name:............{lastName}
        Age:..................{age}
        Phone:................{phone}
    ''')

# --- End of functions -----

# -- User input -----
n1 = int(input("Enter first number >> "))
n2 = int(input("Enter second number >> "))
name = input("What is your name? >> ")

# -- More Input ----
fname = input('Enter your first name >> ')
lname = input('Enter your last name >> ')
age = int(input('Enter your age >> '))
phone= input('Enter your phone >> ')
# -- End of user input

# -- Calling functions -------
addition = add(n1, n2)
subtraction = subtract(n1, n2)
multiplication = multiply(n1, n2)
division = divide(n1, n2)
modulus = printModulus(n1, n2)



# ---- Printing values ------
print('')
print(Fore.BLUE) # changes text color to blue
print('The sum is {}'.format(addition))
print('The subtraction is {}'.format(subtraction))
print('The multiplication is {}'.format(multiplication))
print('The division is {}'.format(division))
print('The modulus is {}'.format(modulus))
print(Style.RESET_ALL) # resets text color to normal
print('')
printName(name)
print(Style.RESET_ALL)
print('')

displayPersonalInfo(fname, lname, age, phone)

 
