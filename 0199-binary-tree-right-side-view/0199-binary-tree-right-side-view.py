# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        level_map = {}
        def dfs(root, k):
            if not root:
                return
            if k not in level_map:
                level_map[k] = root.val
            dfs(root.right, k+1)
            dfs(root.left, k+1)
        dfs(root, 0)
        return list(level_map.values())