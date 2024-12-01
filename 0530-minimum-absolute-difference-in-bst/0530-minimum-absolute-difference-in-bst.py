# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.min = 100000
        self.prev = None
        def minimum(root):
            if not root:
                return
            minimum(root.left)
            if self.prev:
                self.min = min(self.min, root.val - self.prev.val)
                self.prev = root
            else:
                self.prev = root
            minimum(root.right)
        minimum(root)
        return self.min
