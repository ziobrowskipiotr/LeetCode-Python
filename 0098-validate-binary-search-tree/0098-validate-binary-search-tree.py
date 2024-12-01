# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = None
        self.result = True
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            if self.result:
                if self.prev:
                    if self.prev.val >= root.val:
                        self.result = False
                        return
                    else:
                        self.prev = root
                else:
                    self.prev = root
                inorder(root.right)
            else:
                return
        inorder(root)
        return self.result