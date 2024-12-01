# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.result = None
        def postorder(root):
            if not root:
                return None
            left = postorder(root.left)
            right = postorder(root.right)
            if not self.result:
                print(root.val, left, right)
                if (left == p.val and root.val == q.val) or (left == q.val and root.val == p.val) or (right == p.val and root.val == q.val) or (right == q.val and root.val == p.val) or (left == p.val and right == q.val) or (left == q.val and right == p.val):
                    self.result = root
                    return None
                if left in (p.val, q.val):
                    return left
                if right in (p.val, q.val):
                    return right
                if root.val in (p.val, q.val):
                    return root.val
                if root.val in (p.val, q.val):
                    return root.val
                return None



        postorder(root)
        return self.result
