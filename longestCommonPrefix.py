# leetcode easy

def longestCommonPrefix(strs):
    result = ''
    if len(strs) < 1:
        result = ''
    elif len(strs) == 1:
        if len(strs[0]) >= 1:
            result += strs[0][0]
        else:
            result == ''
    else:
        for i in range(len(strs)-1):
            if strs[i][:1] == strs[i+1][:1] and len(strs[i]) >= 1 and len(strs[i+1]) >= 1:
                result += strs[0][:2]
                break
            elif strs[i][0] == strs[i+1][0] and len(strs[i]) >= 1 and len(strs[i+1]) >= 1:
                result += strs[0]
            else:
                result = ''
    return result

print(longestCommonPrefix(['dog', 'racecar', 'car']))
print(longestCommonPrefix(['flower', 'flow', 'flight']))
print(longestCommonPrefix(['a']))
print(longestCommonPrefix(['', 'b']))
