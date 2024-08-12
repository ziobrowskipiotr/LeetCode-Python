# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        while True:
            if head is not None and type(head.val) == int:
                head.val = "x"
                head = head.next
            elif head is None:
                return False
                break
            else:
                return True
                break
