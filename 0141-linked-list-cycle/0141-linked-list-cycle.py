# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is not None:
            if head.next is not None:
                i = 0
                while True:
                    if head is not None and type(head.val) == int:
                        head.val = "x"+str(i)
                        head = head.next
                        i+=1
                    elif head is None:
                        return False
                        break
                    else:
                        pos = int(head.val[1:])
                        return True
                        break
            else:
                pos = -1
                return False
        else:
            return False