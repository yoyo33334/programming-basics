import os 
from os import system
from colorama import Fore, Back, Style

system('clear')

integerNumber = 4 # => integer type with 32 bits => 4 bytes
longNumber = 2905467382992010394765234723472937429734 # => long type with 64 bits => 8 bytes
decimalNumber = 2.54 # => float type with 32 bits => 4 bytes
stringType = "My dog is beautiful" # string is a class
anotherString = "56"
isTrue = True
isStudent = False 
isConnected = False
isInClass = True

print(Fore.CYAN, """
            Integer =>  {integerNumber}
            Long =>  {longNumber}
            Decimal =>  {decimalNumber}
            Another String =>  {anotherString}
            Boolean 1 =>  {isTrue}
            Boolean 2 =>  {isStudent}
            Boolean 3 =>  {isConnected}
            Boolean 4 =>  {isInClass}
""")
print(Style.RESET_ALL)
# print(f"")
# print(f"Decimal =>  {decimalNumber}")
# print(f"String =>  {stringType}")
# print(f"Another String =>  {anotherString}")
# print(f"Boolean 1 =>  {isTrue}")
# print(f"Boolean 2 =>  {isStudent}")
# print(f"Boolean 3 =>  {isConnected}")
# print(f"Boolean 4 =>  {isInClass}")

print(Fore.RED)
print(type(integerNumber))
print(type(longNumber))
print(type(isTrue))
print(type(anotherString))


# assignment 
counter = 1

number_of_iterations = int(input('Please enter the # of iterations >> '))

for i in range(number_of_iterations):
    print('Value of count is {}'.format(counter))
    counter+=1







