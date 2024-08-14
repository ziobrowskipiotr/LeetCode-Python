# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def number_of_nodes(self, head: Optional[ListNode],) -> Optional[int]:
        i = 0
        h = head
        while h is not None:
            i+=1
            h = h.next
        return i
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k > 0 and head is not None and head.next is not None:
            cur = head.next
            prev = head
            num = Solution.number_of_nodes(self, head)
            for i in range(k%num):
                while cur.next is not None:
                    prev = prev.next
                    cur = cur.next
                cur.next, prev.next = head, None
                head, prev, cur = cur, cur, cur.next
        return head
                          