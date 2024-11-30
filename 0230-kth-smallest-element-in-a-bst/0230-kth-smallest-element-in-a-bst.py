# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = [k, None]
        def dfs(root):
            if root.left:
                dfs(root.left)
                result[0] -= 1

            if result[0] == 1:
                result[1] = root.val

            if root.right:
                result[0] -= 1
                dfs(root.right)

        dfs(root)
        return result[1]
