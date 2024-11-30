# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None
        else:
            Node = TreeNode(postorder.pop())
            pivot = inorder.index(Node.val)
            Node.right = self.buildTree(inorder[pivot+1:], postorder)
            Node.left = self.buildTree(inorder[:pivot], postorder)
            return Node
