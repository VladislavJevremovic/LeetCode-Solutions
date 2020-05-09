# https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False

        slow_p = fast_p = head
        while fast_p and fast_p.next:
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slowp == fastp:
                return True

        return False