# https://leetcode.com/problems/delete-node-in-a-linked-list/

class Solution:
	def deleteNode(self, node):
		processed_node = None
		while node and node.next:
			node.val = node.next.val
			processed_node = node
			node = node.next
		processed_node.next = None