# given two non-empty linked lists representing two non-negative numbers
# the digits are stored in reverse order, and each of their nodes contains a single digit
# add the two numbers and return the sum as a linked list

l1 = [2,4,3]
l2 = [5,6,4]
# result should be [7,0,8]

def addTwoNumbers(l1, l2):
    s1, s2 = '', ''
    total = 0
    for num1 in l1:
        s1 += str(num1)
    for num2 in l2:
        s2 += str(num2)
    return list(reversed(str(int(s1) + int(s2))))

print(addTwoNumbers([2,4,3], [5,6,4]))
print(addTwoNumbers([9,9,9,9,9,9,9], [9,9,9,9]))