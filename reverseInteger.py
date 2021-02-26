# easy leetcode
# 36ms
def reverseInteger(x):
    reverse_string = str(x)[::-1]
    reverse_num = 0
    if x > 0 and x <= 2**31 - 1:
        reverse_num = int(reverse_string)
    elif x < 0 and x >= -2**31:
        reverse_num = -1 * int(reverse_string[:len(reverse_string)-1])
    if -2**31 <= reverse_num and reverse_num <= 2**31 - 1:
        return reverse_num
    else:
        return 0

print(reverseInteger(-123))
