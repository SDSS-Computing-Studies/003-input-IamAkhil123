#! python3

import math

print("Enter value of one short side")
a = input()
print("Enter value of another short side")
b = input()

e = a*2 + b*2

number = int(input(e))
sqrt = number ** 0.5

print(sqrt)

# Find the hypotenuse
# Your program will ask the user to enter in the 2 short sides of a right triangle.
# You will calculate the length of the hypotenuse and display the result.
# You will need to use the math module to use the command that finds the square root.
#
# Inputs:
# side, side
#
# Outputs:
# hypotenuse
#
# Test output
# input sides of 5 and 7 should give hypotenuse of 8.60232526704
