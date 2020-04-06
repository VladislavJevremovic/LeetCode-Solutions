// https://leetcode.com/problems/add-two-numbers

class Solution {
    func addTwoNumbers(_ l1: ListNode?, _ l2: ListNode?) -> ListNode? {
        let dummy_head = ListNode(0)
		var p = l1, q = l2, curr: ListNode? = dummy_head
		var carry = 0
		while p != nil || q != nil {
			var sum = carry
			if p != nil {
				sum += p!.val
				p = p?.next
            }
			if q != nil {
				sum += q!.val
				q = q?.next
            }

			curr?.next = ListNode(sum % 10)
			curr = curr?.next
			
			carry = sum / 10
        }

		if carry > 0 {
			curr?.next = ListNode(carry)
        }

		return dummy_head.next
    }
}