#########
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if not head:
            return head
	
        prev, cur = None, head
	
        while left > 1:
            prev = cur
            cur = cur.next
            left -= 1
            right -= 1

        con, tail = prev, cur
        while right > 0:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
            right -= 1
	
        tail.next = cur
        if con:
            con.next = prev
            return head
        else:
            return prev