# easy leetcode

# 60ms
def palindromeNumber(x):
    if x < 0:
        return False
    else:
        reverseNum = int(str(x)[::-1])
        if reverseNum == x and reverseNum <= 2**31 - 1 and -2**31 <= reverseNum:
            return True
        else:
            return False

print(palindromeNumber(123))
print(palindromeNumber(121))