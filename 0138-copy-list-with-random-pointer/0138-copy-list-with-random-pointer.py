"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
##########
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if head is None:
            return head

        h, nex = head, head
        while nex is not None:
            cp = Node(0)
            cp.val = h.val
            nex, nex_c = h.next, cp.next
            h.next, cp.next = cp, nex
            h, cp = nex, nex_c

        h = head
        while h is not None:
            if h.random is not None:
                h.next.random = h.random.next
            else:
                h.next.random = None
            h = h.next.next

        h, cp, copy = head, head.next, head.next
        while cp.next is not None:
            h.next, cp.next = h.next.next, cp.next.next
            h, cp = h.next, cp.next
        else:
            h.next = None

        return copy
        
