# Leetcode easy
# Return the index of the first occurrence of needle in haystack, 
# or -1 if needle is not part of haystack.

def strStr(haystack, needle):
    if needle in haystack:
        return haystack.index(needle)
    elif needle == '':
        return 0
    else:
        return -1

print(strStr('aaaaa', 'bba'))