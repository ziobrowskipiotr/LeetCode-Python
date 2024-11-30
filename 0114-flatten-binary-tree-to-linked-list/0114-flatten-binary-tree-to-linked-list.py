# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        right_node_list = []
        def connect(root):
            if not root:
                return
            if root.right:
                right_node_list.append(root.right)
            if root.left:
                root.right = root.left
                root.left = None
                connect(root.right)
            else:
                if right_node_list:
                    root.right = right_node_list.pop()
                    connect(root.right)
                else:
                    return
        connect(root)

        