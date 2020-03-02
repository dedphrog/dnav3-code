"""Intro to Python - Part 1 - Hands-On Exercise."""
# Mar-02-2020 Pycharm testing.

import math
import random

# Python program to print 
# colored text and background 
class colors: 
    reset='\033[0m'
    bold='\033[01m'
    disable='\033[02m'
    underline='\033[04m'
    reverse='\033[07m'
    strikethrough='\033[09m'
    invisible='\033[08m'
    class fg: 
        black='\033[30m'
        red='\033[31m'
        green='\033[32m'
        orange='\033[33m'
        blue='\033[34m'
        purple='\033[35m'
        cyan='\033[36m'
        lightgrey='\033[37m'
        darkgrey='\033[90m'
        lightred='\033[91m'
        lightgreen='\033[92m'
        yellow='\033[93m'
        lightblue='\033[94m'
        pink='\033[95m'
        lightcyan='\033[96m'
    class bg: 
        black='\033[40m'
        red='\033[41m'
        green='\033[42m'
        orange='\033[43m'
        blue='\033[44m'
        purple='\033[45m'
        cyan='\033[46m'
        lightgrey='\033[47m'



# Create a module variable
module_variable = "I am a module variable."



# This is how to DEBUG your code
print(colors.fg.green,"DEBUG: module_variable =", module_variable)



# Define a function that expects to receive a value for an argument variable
def my_function(argument_variable):
    """Showing how module, argument, and local variables are used."""
    # Create a local variable
    print("DEBUG: ==> Starting my_function()")
    # SPACER 
    print()
    
    local_variable = "I am a local variable."

    print(module_variable, "...and I can be accessed inside a function.")
    print(argument_variable, "...and I can be passed to a function.")
    print(local_variable, "...and I can ONLY be accessed inside a function.")



# Call the function; supplying the value for the argument variable
my_function(argument_variable="I am a argument variable.")



# Let's try accessing that local variable here at module scope
print("\nTrying to access local_variable outside of its function...")
try:
    print(local_variable)
except NameError as error:
    print(error)



# SPACER 
print()
print()



print(colors.fg.red,"Write a print statement that displays both the type and value of `pi`",colors.fg.lightgrey)
pi = 3.14159
print(f'PI is approximately equal to {pi}')
print(f'Python stores this type of data as {type(pi)}')



# SPACER 
print()
print()



print(colors.fg.red,"Write a conditional to print out if `i` is less than or greater than 50",colors.fg.lightgrey)
i = random.randint(0, 100)

if i > 50:
    print("The random interger generator rolled greater than 50")
else:
    print("The random interger generator rolled less than 50")
    
# SPACER 
print()
print()



print(colors.fg.red,"Write a conditional that prints the color of the picked fruit",colors.fg.lightgrey)
picked_fruit = random.choice(['orange', 'strawberry', 'banana'])

if picked_fruit == 'orange':
    print('The random fruit picker found an orange')
if picked_fruit == 'strawberry':
    print('The random fruit picker found a strawberry') 
if picked_fruit == 'banana':
    print('The random fruit picker found a banana') 

# SPACER 
print()
print()



print(colors.fg.red,"Write a function that multiplies two numbers and returns the result.",colors.fg.lightgrey)
# Define the function here.

def number_multiplier(a, b):
    return a * b

# TODO: Now call the function a few times to calculate the following answers
print("Now call the function a few times to calculate the following answers:",colors.fg.lightgrey)


# 12 x 96 =
a = 12
b = 96
x = number_multiplier(a,b)
print(f'12 x 96 = {x}')
print()


# 48 x 17 =
a = 48
b = 17
x = number_multiplier(a,b)
print(f'48 x 17 = {x}')


print()
# 196523 x 87323 =
a = 196523
b = 87323
x = number_multiplier(a,b)
print(f'196523 x 87323 = {x}')


# SPACER 
print()
print()



# TODO: Implement a FOR loop using range()
print(colors.fg.red,"Now implement a FOR loop using range()",colors.fg.lightgrey)

for individual_item in range(5):
    print('This is a scentence to be repeated.')
    
# SPACER 
print()
print()


# TODO: Implement a FOR loop using a varible
# variable name is 'name'
# thing to be iterated is 'names' which is datatype: list
print(colors.fg.red,"Implement a FOR loop using a varible",colors.fg.lightgrey)

names = ["chris", "iftach", "jay"]
print(f'variable name is datatype {type(names)}')

for name in names:
    print(name)
    
# SPACER 
print()
print()


# TODO: Iterate through a dictionary, returning the keys
print(colors.fg.red,"Iterate through a dictionary, returning the keys:",colors.fg.lightgrey)

fruit_inventory = {"apples": 5, "pears": 2, "oranges": 9}
for fruit in fruit_inventory:
     print(fruit)
     print(f"  variable 'fruit' is datatype {type(fruit)}")
     
# SPACER 
print()
print()


# TODO: Iterate through a dictionary, returning the keys and values using the .items() dictionary method
print(colors.fg.red,"Iterate through a dictionary, returning the keys and values using the .items() dictionary method:",colors.fg.lightgrey)
print(colors.fg.green,f"  Variable 'fruit' is datatype {type(fruit)}")
print(colors.fg.green,f"  Dictionary 'fruit_inventory' is datatype {type(fruit_inventory)}")

list(fruit_inventory.items())
[('oranges', 9), ('apples', 5), ('pears', 2)]
for fruit in fruit_inventory.items():
     print(colors.fg.lightgrey,fruit,colors.fg.green,f"  variable 'fruit' is datatype {type('apples')}")


# SPACER 
print()
print()


# Use unpacking 
print(colors.fg.red,"Use unpacking ",colors.fg.lightgrey)
a, b, c = [1, 2, 3]
print(a)
print(b)
print(c)

# SPACER 
print()
print()

# Use unpacking to unpack those key value pairs into a varable name
print(colors.fg.red,"Use unpacking to unpack those key value pairs into a varable name",colors.fg.lightgrey)

for fruit, quantity in fruit_inventory.items():
    print("You have {} {}.".format(quantity, fruit))
    
# SPACER 
print()
print()

# Create a conditional loop
print(colors.fg.red,"Create a conditional loop",colors.fg.lightgrey)
i = 0
while i < 5:
    print(i)
    i += 1

print(f"Loop Stop. The final value for 'i' is {i}")

# Create an infinite loop
#print(colors.fg.lightgrey,"Create an infinite loop")
#from time import sleep
#while True:
#    try:
#        print("Polling.")
#        # Poll some resource
#        sleep(1)
#    except KeyboardInterrupt:
#        break

