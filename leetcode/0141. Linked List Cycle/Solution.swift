// https://leetcode.com/problems/linked-list-cycle/

public class ListNode {
    public var val: Int
    public var next: ListNode?
    public init(_ val: Int) {
        self.val = val
        self.next = nil
    }
}

class Solution {
    func hasCycle(_ head: ListNode?) -> Bool {
        guard let head = head else {
            return false
        }

        var slowp: ListNode? = head
        var fastp: ListNode? = head

        while fastp != nil && fastp?.next != nil {
            slowp = slowp?.next
            fastp = fastp?.next?.next

            if slowp === fastp {
                return true
            }
        }

        return false
    }
}

extension Solution {
    func makeList(_ array: [Int], _ pos: Int) -> ListNode? {
        var head: ListNode? = ListNode(0)
        let originalHead = head
        var i = 0
        var cycleEndNode: ListNode?
        for n in array {
            if i == pos {
                cycleEndNode = head
            }
            head?.next = ListNode(n)
            head = head?.next
            i += 1
        }
        if pos >= 0 {
            head?.next = cycleEndNode
        }

        return originalHead?.next
    }
}

let s = Solution()
assert(s.hasCycle(s.makeList([3,2,0,-4], 1)) == true)
assert(s.hasCycle(s.makeList([1,2], 0)) == true)
assert(s.hasCycle(s.makeList([1], -1)) == false)
