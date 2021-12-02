#! python3
import math
#### Task 4
"""
Find the hypotenuse\
Your program will ask the user to enter in the 2 short sides of a right triangle.\
You will calculate the length of the hypotenuse and display the result.\
You will need to use the *math* module to use the command that finds the square root.\
(2 points)
"""
print("Enter value of one short side")
a = input()
print("Enter value of another short side")
b = input()

e = float(a) * float(a) + float(b) * float(b)

print (math.sqrt(e))

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
