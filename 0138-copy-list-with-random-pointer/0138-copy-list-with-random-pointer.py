"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        result_list = Node(0)
        copy_head = result_list
        new_node = Node(0)

        while head is not None:
            copy_head.val = head.val
            copy_head.random = head.random

            head_temp = head
            head = head.next
            head_temp.next = copy_head

            if head is not None:
                copy_head.next = new_node
                copy_head = copy_head.next
                new_node = Node(0)
		
        copy_head = result_list

        while copy_head is not None:
            if copy_head.random is not None:
                copy_head.random = copy_head.random.next
            copy_head = copy_head.next

        return result_list	