# leetcode easy

def longestCommonPrefix(strs):
    # no string = no prefix
    if len(strs) == 0:
        return ""

    # compare other strings to the very first one
    hold = strs[0]

    for i in range(1, len(strs)):
        prefix = ''

        # if the first string is empty, there is no common prefix
        if len(hold) == 0:
            break
        
        for j in range(len(strs[i])):
            
            if j < len(hold) and hold[j] == strs[i][j]:
                prefix += hold[j]
            else:
                break
        hold = prefix
    return hold

print(longestCommonPrefix(['dog', 'racecar', 'car']))
print(longestCommonPrefix(['flower', 'flow', 'flight']))
print(longestCommonPrefix(['a']))
print(longestCommonPrefix(['', 'b']))
print(longestCommonPrefix(['reflower', 'flow', 'flight']))
