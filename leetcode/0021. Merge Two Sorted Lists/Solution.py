# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None: 
            return l2 

        if l2 is None: 
            return l1 

        temp = None
        if l1.val <= l2.val:
            temp = l1
            temp.next = self.mergeTwoLists(l1.next, l2)
        else:
            temp = l2
            temp.next = self.mergeTwoLists(l1, l2.next)

        return temp
