# Leetcode easy

# Given a non-empty array of decimal digits representing a non-negative integer, 
# increment one to the integer.

# The digits are stored such that the most significant digit is at the head of the list, 
# and each element in the array contains a single digit.

# You may assume the integer does not contain any leading zero, except the number 0 itself.

def plusOne(digits):
    numS = ''
    numI = ''
    result = []
    for num in digits:
        numS += str(num)
    numI = str(int(numS) + 1)
    for i in range(len(numI)):
        result.append(numI[i])
    return result

print(plusOne([1,2,9]))