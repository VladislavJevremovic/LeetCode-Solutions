# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        
        fast_p = slow_p = dummy
        for i in range(1, n + 2):
            fast_p = fast_p.next
            
        while fast_p:
            fast_p = fast_p.next
            slow_p = slow_p.next
            
        slow_p.next = slow_p.next.next
        
        return dummy.next