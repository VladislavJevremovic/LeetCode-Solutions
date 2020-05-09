# https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        
        stack = []
        
        p = head
        while p:
            stack.append(p.val)
            p = p.next
            
        p = head
        while p:
            t = stack.pop()
            if t != p.val:
                return False
            p = p.next
        
        return True