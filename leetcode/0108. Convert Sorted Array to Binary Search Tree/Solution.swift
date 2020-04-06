// https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

class Solution {
    func sortedArrayToBST(_ nums: [Int]) -> TreeNode? {
        return sortedArrayToBST(nums, 0, nums.count - 1)
    }

    func sortedArrayToBST(_ nums: [Int], _ low: Int, _ high: Int) -> TreeNode? {
        if low > high {
            return nil
        }

        let mid = low + (high - low) / 2
        let root = TreeNode(nums[mid])
        root.left = sortedArrayToBST(nums, low, mid - 1)
        root.right = sortedArrayToBST(nums, mid + 1, high)

        return root
    }
}