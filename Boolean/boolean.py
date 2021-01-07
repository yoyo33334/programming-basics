import os
from os import system

system('clear')

isFromNCI = False

name = str(input("Enter your name >> "))

if(name == 'Aicha' or name == 'Daniel' or name == 'Pushpa'):
    isFromNCI = True


if(isFromNCI):
    print('{} studies at NCI'.format(name))
else:
    print('{} does not study at NCI'.format(name))

