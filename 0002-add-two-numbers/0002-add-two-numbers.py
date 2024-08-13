# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list_head = ListNode()
        list_node = list_head
        prev1 = l1
        curr1 = l1.next
        prev2 = l2
        curr2 = l2.next
        while curr1 is not None:
            next1 = curr1.next
            curr1.next = prev1
            l1.next = next1
            prev1, curr1 = curr1, next1
        while curr2 is not None:
            next2 = curr2.next
            curr2.next = prev2
            l2.next = next2
            prev2, curr2 = curr2, next2
        while prev1 is not None and prev2 is not None:
            list_node.next = ListNode()
            if prev1.val + prev2.val >= 10:
                list_node.next.val = prev1.val + prev2.val - 10
                if prev1.next is None:
                    prev1.next = ListNode()
                prev1.next.val += 1
            else:
                list_node.next.val = prev1.val + prev2.val
            prev1, prev2, list_node = prev1.next, prev2.next, list_node.next
        if prev1 is None and prev2 is None:
            return list_head.next
        elif prev1 is None:
            while prev2 is not None:
                if prev2.val == 10:
                    if prev2.next is None:
                        prev2.next = ListNode()
                    prev2.next.val += 1
                    prev2.val = 0
                list_node.next = prev2
                list_node, prev2 = list_node.next, prev2.next
            return list_head.next
        elif prev2 is None:
            while prev1 is not None:
                if prev1.val == 10:
                    if prev1.next is None:
                        prev1.next = ListNode()
                    prev1.next.val += 1
                    prev1.val = 0
                list_node.next = prev1
                list_node, prev1 = list_node.next, prev1.next
            return list_head.next


        
        
        
