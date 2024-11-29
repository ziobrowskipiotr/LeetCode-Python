#########
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if left == right:
            return head

        current_node = head
        left_node = head
        right_node = head
        before_left = head
        after_right = head
        prev_node = head
        ix = 1
        
        while current_node is not None:
            if ix == left-1:
                before_left = current_node
                current_node = current_node.next
            elif ix == right+1:
                after_right = current_node
                current_node = current_node.next
            elif ix == left:
                prev_node = current_node
                left_node = current_node

                temp_node = current_node
                current_node = current_node.next
                temp_node.next = None
            elif ix > left and ix < right:
                temp_node = current_node
                current_node = current_node.next
                temp_node.next = prev_node
                prev_node = temp_node
            elif ix == right:
                right_node = current_node
                temp_node = current_node

                current_node = current_node.next
                temp_node.next = prev_node
                prev_node = temp_node
            else:
                current_node = current_node.next
            ix += 1

        if left != 1:
            before_left.next = right_node
        if right != ix-1:
            left_node.next = after_right

        if left == 1:
            return right_node
        else:
            return head