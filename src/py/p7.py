# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,??Y-1.
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]


def two_d_array(n1,n2):
    out = []
    for i in range(0,n1):
        inner = []
        for j in range(0,n2):
            inner.append(i*j)
        out.append(inner)
    return out

print(two_d_array(3,5))

# $ python p7.py
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]