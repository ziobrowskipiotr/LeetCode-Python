# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {}
        for i in range(len(inorder)):
            inorder_map[inorder[i]] = i

        def build(left, right) -> Optional[TreeNode]:
            if left > right:
                return None
            else:
                Node = TreeNode(preorder.pop(0))
                mid = inorder_map[Node.val]
                Node.left = build(left, mid-1)
                Node.right = build(mid+1, right)
                return Node

        return build(0, len(preorder)-1)