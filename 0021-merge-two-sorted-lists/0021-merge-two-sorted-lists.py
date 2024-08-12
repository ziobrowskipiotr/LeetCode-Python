# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node_start = ListNode()
        node = node_start
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            elif list2.val < list1.val:
                node.next = list2
                list2 = list2.next
            else:
                node.next = list1
                list1 = list1.next
                node = node.next
                node.next = list2
                list2 = list2.next
            node = node.next
        if list1 is None:
            node.next = list2
        elif list2 is None:
            node.next = list1

        return node_start.next