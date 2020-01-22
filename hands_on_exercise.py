"""Intro to Python - Part 1 - Hands-On Exercise."""


import math
import random

print()

print("# TODO: Write a print statement that displays both the type and value of `pi`")
pi = 3.14159
print(f'PI is approximately equal to {pi}')
print(f'Python stores this type of data as {type(pi)}')

print()


print("# TODO: Write a conditional to print out if `i` is less than or greater than 50")
i = random.randint(0, 100)

if i > 50:
    print("The random interger generator rolled greater than 50")
else:
    print("The random interger generator rolled less than 50")
    
print()


print("# TODO: Write a conditional that prints the color of the picked fruit")
picked_fruit = random.choice(['orange', 'strawberry', 'banana'])

if picked_fruit == 'orange':
    print('The random fruit picker found an orange')
if picked_fruit == 'strawberry':
    print('The random fruit picker found a strawberry') 
if picked_fruit == 'banana':
    print('The random fruit picker found a banana') 

print()

print("# TODO: Write a function that multiplies two numbers and returns the result")
# Define the function here.

def number_multiplier(a, b):
    return a * b

    


# TODO: Now call the function a few times to calculate the following answers

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


print()
