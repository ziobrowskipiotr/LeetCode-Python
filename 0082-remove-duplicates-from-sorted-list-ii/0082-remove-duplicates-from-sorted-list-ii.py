# ####
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        dummy = ListNode()
        dummy.next, current_node, prev_node = head, head, dummy
		
        while current_node is not None and current_node.next is not None:
            if current_node.val == current_node.next.val:
                while current_node.next is not None and current_node.val == current_node.next.val:
                    current_node = current_node.next
                current_node = current_node.next
                prev_node.next = current_node
            else:
                prev_node = prev_node.next
                current_node = current_node.next
        return dummy.next
            
