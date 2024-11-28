#######################################
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current_node = ListNode()
        first_node = current_node
        add_number = 0
        while l1 != None or l2 != None or add_number:
            cur_val1 = l1.val if l1 != None else 0
            cur_val2 = l2.val if l2 != None else 0
            new_node = ListNode((cur_val1 + cur_val2 + add_number)%10)
            add_number = (cur_val1 + cur_val2 + add_number)//10
            current_node.next = new_node
            current_node = new_node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return first_node.next
