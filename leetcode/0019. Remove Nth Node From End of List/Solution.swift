// https://leetcode.com/problems/remove-nth-node-from-end-of-list

public class ListNode {
    public var val: Int
    public var next: ListNode?
    public init(_ val: Int) {
        self.val = val
        self.next = nil
    }
}

class Solution {
    func removeNthFromEnd(_ head: ListNode?, _ n: Int) -> ListNode? {
        var p1 = head
        var p2 = head

        for _ in 0..<n {
            p1 = p1?.next
        }
        
        var prev: ListNode? = nil
        while p1 != nil {
            p1 = p1?.next
            prev = p2
            p2 = p2?.next
        }

        var head = head
        if prev != nil {
            prev?.next = p2?.next
        } else {
            head = head?.next
        }
        
        return head
    }
}
