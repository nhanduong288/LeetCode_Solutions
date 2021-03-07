# leetcode easy
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid.

def validParentheses(s):
    # using stack solution
    # a dictionary for all the parentheses
    par_dict = {'(':')', '[':']', '{':'}'}
    # a stack to keep track of the parentheses
    par_stack = []
    open_par = '({['
    for par in s:
        if par in open_par:
            # append open parentheses to the stack
            par_stack.append(par)
        # finding closed parenthesis in the string to match open parenthesis from back to top
        # to make sure they are valid parentheses 
        elif par_stack and par == par_dict[par_stack[-1]]:
            par_stack.pop()
        else:
            return False
    return par_stack == []



print(validParentheses('()')) # true
print(validParentheses('()[]{}')) # true
print(validParentheses('{[]}')) # true
print(validParentheses('(]')) # false
print(validParentheses('([)]')) # false
print(validParentheses('(){}}{')) # false
print(validParentheses('(([]){})')) # true
