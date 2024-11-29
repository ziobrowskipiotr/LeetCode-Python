# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        def reverse_list(prev, cur, k):
            con, tail = prev, cur
            while k:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
                k -= 1
            tail.next = cur
            if con:
                con.next = prev
            return tail

        left, cur, prev = head, head, None
        reverse_ix = 0
        ix = 1
        while cur:
            if ix < k:
                cur = cur.next
                ix += 1
            elif ix == k:
                if reverse_ix == 0:
                    head = cur
                    reverse_ix += 1
                prev = reverse_list(prev=prev, cur=left, k=k)
                left, cur = prev.next, prev.next
                ix = 1
        return head
