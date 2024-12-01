# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        def dfs(root, k):
            if not root:
                return
            if k == len(result):
                result.append([root.val])
            else:
                result[k] += [root.val]
            dfs(root.left, k+1)
            dfs(root.right, k+1)
        dfs(root, 0)
        return result