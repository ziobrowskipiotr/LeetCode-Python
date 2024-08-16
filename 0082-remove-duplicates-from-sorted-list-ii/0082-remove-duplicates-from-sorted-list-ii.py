# ##############
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        cur = head
        nex = head.next
        prev = None
        i = False

        while nex is not None:
            if cur.val == nex.val:
                nex = cur
                while cur.val == nex.val:
                    cur, nex = nex, nex.next
                    if nex is not None:
                        cur.next = None
                    else:
                        if prev is None:
                            return None
                        else:
                            prev.next = None
                            return head
                cur, nex = nex, nex.next
                if i == False:
                    head = cur
                if prev is not None:
                    prev.next = cur
            else:
                prev, cur, nex = cur, cur.next, nex.next
                i = True

        return head
