# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        level_map = collections.defaultdict(list)
        def dfs(root, k):
            if not root:
                return
            level_map[k] += [root.val]
            dfs(root.left, k+1)
            dfs(root.right, k+1)
        
        dfs(root, 0)
        return [mean(cur_list) for cur_list in level_map.values()]