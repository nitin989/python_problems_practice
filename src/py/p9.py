# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT

lines = []
while True:
    input_str = input("Please enter a string :- ")
    if input_str:
        lines.append(input_str.upper())
    else:
        break

for line in lines:
    print(line)

# $ python p9.py
# Please enter a string :- hello world
# Please enter a string :- practice makes perfect
# Please enter a string :-
# HELLO WORLD
# PRACTICE MAKES PERFECT