# https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        odd_list = ListNode(0)
        even_list = ListNode(0)
        
        odd_head = odd_list
        even_head = even_list
        
        is_odd = True
        while head:
            if is_odd:
                odd_list.next = head
                odd_list = odd_list.next
            else:
                even_list.next = head
                even_list = even_list.next
            
            is_odd = not is_odd
            head = head.next
        
        even_list.next = None
        odd_list.next = even_head.next
        
        return odd_head.next