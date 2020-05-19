# Question:
# Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world

def sort_remove_dups(str):
    out_list = []
    inp_list = str.split(' ')
    for s in inp_list:
        out_list.append(s)
    return sorted(set(out_list))

str = input("Enter a string :- ")
print(' '.join(sort_remove_dups(str)))

# $ python p10.py
# Enter a string :-  hello world and practice makes perfect and hello world again
#  again and hello makes perfect practice world