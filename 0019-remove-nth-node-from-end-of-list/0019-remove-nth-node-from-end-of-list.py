#########################################
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def number_of_nodes(self, head: Optional[ListNode]) -> Optional[int]:
        h = head
        i = 0
        while h is not None:
            i+=1
            h = h.next
        return i
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        num = Solution.number_of_nodes(self, head)
        if num < 2:
            return None

        k = num - n
        if k == 0:
            head = head.next
        else:
            h = head
            for i in range(k):
                if i == k-1:
                    h.next = h.next.next
                h = h.next
        return head


