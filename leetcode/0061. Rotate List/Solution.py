// https://leetcode.com/problems/rotate-list

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head == None or k == 0:
            return head

        counter = head
        length = 0
        while counter:
            length += 1
            tail = counter
            counter = counter.next

        if length == 1:
            return head
            
        l_rotations = length - k % length
        
        result = head
        while l_rotations > 0:
            chopped_head = result
            remainder = result.next
            
            chopped_head.next = None
            tail.next = chopped_head
            tail = tail.next
            
            result = remainder
            l_rotations -= 1
        
        return result