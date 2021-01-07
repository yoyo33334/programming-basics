import os 
from os import system 

system('clear') # => linux or mac
# system('cls') => Windows

# This prints all even and odd numbers from 0 to 4
for i in range(5):
    if(i % 2 == 0):
        print("even =>  {}".format(i))
    else:
        print("odd => {}".format(i))


