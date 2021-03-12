# Leetcode easy

# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. 
# In how many distinct ways can you climb to the top?

# Fibonacci number approach
def climbStairs(n):
    if n <= 2:
        return n
    x, y = 1, 2
    for i in range(3, n):
        tmp = y
        y += x
        x = tmp
    return (x+y)

print(climbStairs(4))    