# Question:
# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world

user_input = input("Enter sequenece of words seperated by comma:- ").split(',')
print(",".join(sorted(user_input)))

# $ python p8.py
# Enter sequenece of words seperated by comma:- without,hello,bag,world
# bag,hello,without,world