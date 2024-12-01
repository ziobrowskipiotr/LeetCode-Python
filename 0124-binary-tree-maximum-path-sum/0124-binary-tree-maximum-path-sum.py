# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.result = -float('inf')
        def postorder(root):
            if not root:
                return 0
            left = postorder(root.left)
            right = postorder(root.right)
            self.result = max(self.result, left+right+root.val, left+root.val, right+root.val, root.val)
            return max(max(left,right)+root.val, root.val)
        postorder(root)
        return self.result