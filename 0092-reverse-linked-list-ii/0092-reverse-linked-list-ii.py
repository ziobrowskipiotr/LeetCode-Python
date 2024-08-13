##############
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        h = head
        if right-left < 1:
            return head
        if left == 1:
            node_left = None
        for i in range(right):
            if i+2 == left:
                node_left = head
            elif i+1 == left:
                node_h, prev, cur, nex = head, head, head.next, head.next.next
            elif i+1 > left:
                cur.next, node_h.next = prev, nex
                cur, prev = nex, cur
                if i+1 == right:
                    break
                nex = nex.next
            head = head.next
        if node_left is not None:
            node_left.next = prev
            return h
        else:
            return prev