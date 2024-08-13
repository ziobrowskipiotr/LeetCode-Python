# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n_preview = head
        n_current = head.next
        while n_current is not None:
            n_next = n_current.next
            n_current.next = n_preview
            head.next = n_next
            n_preview, n_current = n_current, n_next
        return n_preview

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list_head = ListNode()
        list_node = list_head
        prev1 = Solution.reverse_list(self, l1)
        prev2 = Solution.reverse_list(self, l2)
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
            head = Solution.reverse_list(self, list_head.next)
            return head

        elif prev1 is None:
            while prev2 is not None:
                if prev2.val == 10:
                    if prev2.next is None:
                        prev2.next = ListNode()
                    prev2.next.val += 1
                    prev2.val = 0
                list_node.next = prev2
                list_node, prev2 = list_node.next, prev2.next
            head = Solution.reverse_list(self, list_head.next)
            return head

        elif prev2 is None:
            while prev1 is not None:
                if prev1.val == 10:
                    if prev1.next is None:
                        prev1.next = ListNode()
                    prev1.next.val += 1
                    prev1.val = 0
                list_node.next = prev1
                list_node, prev1 = list_node.next, prev1.next
            head = Solution.reverse_list(self, list_head.next)
            return head
