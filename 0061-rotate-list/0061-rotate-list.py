class Solution:
    def number_of_nodes(self, head: Optional[ListNode]) -> int:
        i = 0
        while head is not None:
            head = head.next
            i += 1
        return i
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        list_len = self.number_of_nodes(head)
        if k%list_len == 0:
            return head
        first_node = head
        current_node = head
        
        ix = 1
        while current_node is not None:
            if ix == list_len-(k%list_len):
                temp_node = current_node
                current_node = current_node.next
                first_node = current_node
                temp_node.next = None
                while current_node.next is not None:
                    current_node = current_node.next
                else:
                    current_node.next = head
                break
            else:
                ix += 1
                current_node = current_node.next
        return first_node
