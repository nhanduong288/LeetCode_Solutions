# leetcode easy
# Merge 2 sorted linked lists and return it as a sorted list
# The list should be made by splicing together the nodes of the first two lists
class ListNode:
    def insert(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoSortedLists(l1, l2):
        '''head = tail = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        tail.next = l1 or l2
        return head.next'''
