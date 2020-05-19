# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320

######## without recursion 

def fact_without_recursion(n):
    if n==0:
        return 1
    fact_out = 1
    while (n>0):
        fact_out = fact_out*n
        n -= 1
    return fact_out


######## with recursion

def fact_with_recursion(n):
    if n==0:
        return 1
    else:
        return n*fact_with_recursion(n-1)


user_num = int(input("Please neter a number :- "))
print(fact_without_recursion(user_num))
print(fact_with_recursion(user_num))

