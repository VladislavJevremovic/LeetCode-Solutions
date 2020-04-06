// https://leetcode.com/problems/delete-node-in-a-linked-list/

class Solution:
	def deleteNode(self, node):
		p = None
		while node and node.next:
			node.val = node.next.val
			p = node
			node = node.next
		p.next = None