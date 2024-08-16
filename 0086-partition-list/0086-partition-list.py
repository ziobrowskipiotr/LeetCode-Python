# ######################################
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        cur, prev = dummy, dummy
        while cur.next is not None:
            if cur.next.val >= x:
                cur, cur.next = cur.next, cur.next.next
            else:
                if cur.next != prev.next:
                    prev.next, cur.next.next, cur.next = cur.next, prev.next, cur.next.next
                    cur.next, prev = cur.next, prev.next
                else:
                    prev, cur, cur.next = prev.next, cur.next, cur.next.next
        return dummy.next
