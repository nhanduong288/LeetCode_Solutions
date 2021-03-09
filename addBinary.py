# Leetcode easy
# Given two binary strings a and b, return their sum as a binary string.

def addBinary(a, b):
    integer_sum = int(a, 2) + int(b, 2)
    binary_sum = bin(integer_sum)
    print(binary_sum)

addBinary('11', '1')