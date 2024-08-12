# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is not None:
            if head.next is not None:
                list = []
                list.append(head)
                pointer = head.next
                list.append(pointer)
                while True:
                    n_pointer = pointer.next
                    if n_pointer is None:
                        return False
                        break
                    elif n_pointer in list:
                        pos = list.index(n_pointer)
                        return True
                        break
                    else:
                        list.append(n_pointer)
                        pointer = n_pointer
            else:
                pos = -1
                return False
        else:
            return False