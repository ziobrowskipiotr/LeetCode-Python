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
		
        def connecting(prev, child_node, most_left):
            if child_node:
                if prev:
                    prev.next = child_node
                else:
                    most_left = child_node
                prev = child_node
			
            return prev, most_left

        most_left = root
        while most_left:
            prev, cur = None, most_left
            most_left = None
            while cur:
                prev, most_left = connecting(prev, cur.left, most_left)
                prev, most_left = connecting(prev, cur.right, most_left)
                cur = cur.next
        return root
				