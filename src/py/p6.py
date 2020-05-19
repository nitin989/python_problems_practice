# Question:
# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# Example
# Let us assume the following comma separated input sequence is given to the program:
# 100,150,180
# The output of the program should be:
# 18,22,24
import math as m
def values_calc(l):
    c = 50
    h = 30
    return ",".join([str(int(m.sqrt(2*c*int(num)/h))) for num in l])

user_input = input("PLEASE ENTER NUMBERS SEPERATED BY COMMA :- ").split(',')
print(values_calc(user_input))

# PLEASE ENTER NUMBERS SEPERATED BY COMMA :- 100,150,180
# 18,22,24