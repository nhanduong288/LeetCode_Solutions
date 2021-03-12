# Leetcode easy
# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. 
# Return the linked list sorted as well.

class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        hold = head
        while hold:
            if hold.next and hold.next.val == hold.val:
                hold.next = hold.next.next
            else:
                hold = hold.next
        return head