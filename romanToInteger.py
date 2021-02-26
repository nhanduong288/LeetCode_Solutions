# leetcode easy

from typing import TYPE_CHECKING


def romanToInteger(s):
    result = 0
    first_half = 0
    second_half = 0
    letter = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

    def minus(s):
        for roman in s[1:]:
            result += -1 + letter[roman]
    
    return result

print(romanToInteger("VII")) 
