"""
Mahafog Risat
Feb 8, 2025
Lab 5, function
"""
import math
from lab5_function_risat import *

print('\n---- Example 1: user-defined function ')
w = 8
length = 3
a = area_rectangle(w,length)
print_area_result(w,length,a)

print('\n---- Example 2: calculate the distance of two points ')
x1 = collectnum('x1')
x2 = collectnum('x2')
y1 = collectnum('y1')
y2 = collectnum('y2')

# testing
# print(f"({x1},{y1}) ({x2},{y2})")

# testing
# print(f"distance = {calculate_distance(x1,x2,y1,y2)}")

distance = calculate_distance(x1,x2,y1,y2)
print_distance(x1,x2,y1,y2,distance)

print('\nEXERCISE')

guess = input("Guess a number between 1 and 10: ")

# generate random number
random_num = generate_random(0, 9)

# testing
print(f"random number = {random_num}")
print(f"guess number = {guess}")

# compare numbers
compare_number(guess, random_num)