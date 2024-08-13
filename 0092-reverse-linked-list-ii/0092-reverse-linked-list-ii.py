# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        h = head
        for i in range(right):
            if i == left-2:
                node_left = head
            if left-1 <= i and i <= right-1:
                if i == left-1:
                    if right-left < 1:
                        return h    
                    elif i == 0:
                        node_left = None
                        node_h = head
                        prev = head
                        cur = head.next
                    else:
                        node_h = head
                        prev = head
                        cur = head.next
                else:
                    nex = cur.next
                    if node_left is not None:
                        cur.next, node_left.next, node_h.next = prev, cur, nex
                    else:
                        cur.next, node_h.next = prev, nex
                        print(cur)
                    if i == right-1:
                        if left == 1:
                            return cur
                        else:
                            break
                    cur, nex, prev = nex, nex.next, cur
            head = head.next
        return h