# Leetcode easy

# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. 
# In how many distinct ways can you climb to the top?

def climbStairs(n):
    # first way is always 1 step at a time
    ways = 1
    