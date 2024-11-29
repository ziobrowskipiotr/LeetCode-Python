######################################
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def number_of_nodes(head):
            ix = 0
            while head is not None:
                ix += 1
                head = head.next
            return ix
        
        len_list = number_of_nodes(head)
        m = len_list-n+1
        current_node = head
        temp_node = head
        ix = 1
        if m == 1:
            return head.next

        while current_node is not None and ix <= m+1:
            if ix == m-1:
                temp_node = current_node
                current_node = current_node.next
                temp_node.next = None
            elif ix == m+1:
                temp_node.next = current_node
                current_node = current_node.next
            else:
                current_node = current_node.next
            ix += 1
        return head


