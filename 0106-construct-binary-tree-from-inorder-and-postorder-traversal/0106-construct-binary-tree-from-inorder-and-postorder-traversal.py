# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {}
        for i in range(len(inorder)):
            inorder_map[inorder[i]] = i

        def build(left, right):
            if left > right:
                return None
            else:
                Node = TreeNode(postorder.pop())
                pivot = inorder_map[Node.val]
                Node.right = build(pivot+1, right)
                Node.left = build(left, pivot-1)
                return Node
        return build(0, len(inorder)-1)
