import os
from os import system

system('clear')

integerArr = (3, 6, 8, 9)  # array of integers
decimalArr = (3.4, 5.4, 7.0, 3.4) # array of floats
booleanArr = (True, True, False, True) # array of booleans
stringArray = ('Dunieski', 'Orlando', 'Martha', 'Yanet') # array of strings
isTrue = False
# print the integerArr
for i in integerArr:
    print(f'Integer value is {i}')
    print('Integer value is {}'.format(i))

print(integerArr)
print("I'm here")
print(type(integerArr))
print(type(isTrue))

value = 5 # assigning values
# if(name == "Cuba") => comparing
if (type(isTrue) == bool):
    print("The value is a boolean")
else:
    print("It is not a boolean")


