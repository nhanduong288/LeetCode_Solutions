# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid.

def validParentheses(s):
    '''for par in s:
        if s.count('(') != s.count(')') or s.count('[') != s.count(']') or s.count('{') != s.count('}'):
            return False
        elif par == '(' and (s.index(')') - s.index('(')) % 2 != 1:
            return False
        elif par == '[' and (s.index(']') - s.index('[')) % 2 != 1:
            return False
        elif par == '{' and (s.index('}') - s.index('{')) % 2 != 1:
            return False
        return True'''
    open_par = '([{'
    ls = list(s)
    print('is this working')
    for thing in ls:
        print('we are here')
        if ls[0] not in open_par:
            return False
        elif ls.count('(') != ls.count(')') or ls.count('[') != ls.count(']') or ls.count('{') != ls.count('}'):
            return False
        else:
            for i in range(len(ls)):
                if ls[i] == '(' and (ls.index(')') - ls.index('(')) % 2 != 1:
                    ls.remove('(')
                    ls.remove(')')
                    print('length (: ' + len(ls))
                elif ls[i] == '{' and (ls.index('}') - ls.index('{')) % 2 != 1:
                    ls.remove('{')
                    ls.remove('}')
                    print('length {: ' + len(ls))
                elif ls[i] == '[' and (ls.index(']') - ls.index('[')) % 2 != 1:
                    ls.remove('[')
                    ls.remove(']')
                    print('length []: ' + len(ls))
    if len(ls) == 0:
        return True
    return False


print(validParentheses('()')) # true
print(validParentheses('()[]{}')) # true
print(validParentheses('{[]}')) # true
print(validParentheses('(]')) # false
print(validParentheses('([)]')) # false
print(validParentheses('(){}}{')) # false
