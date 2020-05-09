# https://leetcode.com/problems/add-two-numbers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head = ListNode(0)
        head = dummy_head
        carry = 0
        while l1 or l2:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l1 = l1.next

            head.next = ListNode(carry % 10)
            head = head.next

            carry //= 10
        
        if carry:
            head.next = ListNode(carry)
        
        return dummy_head.next
