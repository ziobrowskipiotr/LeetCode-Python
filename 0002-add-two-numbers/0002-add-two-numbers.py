#######################################
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list_head = ListNode()
        list_node = list_head
        while l1 is not None and l2 is not None:
            list_node.next = ListNode()
            if l1.val + l2.val >= 10:
                if l1.next is None:
                    l1.next = ListNode()
                list_node.next.val = l1.val + l2.val - 10
                l1.next.val += 1
            else:
                list_node.next.val = l1.val + l2.val
            list_node, l1, l2 = list_node.next, l1.next, l2.next
        if l1 is None and l2 is None:
            return list_head.next
        if l1 is None:
            list_node.next = l2
            return list_head.next
        if l2 is None:
            while l1 is not None:
                if l1.val == 10:
                    if l1.next is None:
                        l1.next = ListNode()
                    l1.next.val += 1
                    l1.val = 0
                list_node.next = l1
                list_node, l1 = list_node.next, l1.next
            return list_head.next
