"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
		
        def connecting(prev, child_node, left):
            if child_node:
                if prev:
                    prev.next = child_node
                else:
                    left = child_node
                prev = child_node
			
            return prev, left

        left = root
        while left:
            prev, cur = None, left
            left = None
            while cur:
                prev, left = connecting(prev, cur.left, left)
                prev, left = connecting(prev, cur.right, left)
                cur = cur.next
        return root
				