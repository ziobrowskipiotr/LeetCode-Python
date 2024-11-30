# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def dfs(root, suma):
            suma = 10*suma + root.val
            if not root.left:
                if not root.right:
                    return suma
                else:
                    return dfs(root.right, suma)
            elif not root.right:
                return dfs(root.left, suma)
            else:
                return dfs(root.left, suma)+dfs(root.right, suma)
        return dfs(root, 0)