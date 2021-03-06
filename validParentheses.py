# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid.

def validParentheses(s):
    par_dict = {'(':')', '[':']', '{':'}'}
    open_par = '({['
    ls = list(s)
    '''print('where am i')
    print(len(ls) > 0)
    print(ls[0] in open_par)
    print((ls.index(ls[0]) - ls.index(par_dict[ls[0]])) % 2 == 1)
    print(ls.index(ls[0]))  
    print(ls.index(')'))'''
    if s.count('(') != s.count(')') or s.count('[') != s.count(']') or s.count('{') != s.count('}'):
        ls = ls
    else:
        while len(ls) > 0 and ls[0] in open_par:
            #print('or am i here')
            ls.remove(par_dict[ls[0]])
            ls.remove(ls[0])    
    return ls == []



print(validParentheses('()')) # true
print(validParentheses('()[]{}')) # true
print(validParentheses('{[]}')) # true
print(validParentheses('(]')) # false
print(validParentheses('([)]')) # false
print(validParentheses('(){}}{')) # false
print(validParentheses('(([]){})')) # true
