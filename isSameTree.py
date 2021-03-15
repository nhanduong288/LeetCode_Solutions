# Leetcode easy

# Given the roots of two binary trees p and q, 
# write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, 
# and the nodes have the same value.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(self, p, q):
    if p is None and q is None:
        return True
    elif p.val != q.val and p is None or q is None:
        return False
    return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
