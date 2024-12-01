# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.nodes_list = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            self.nodes_list.append(root.val)
            inorder(root.right)
        inorder(root)

    def next(self) -> int:
        return self.nodes_list.pop(0) if self.nodes_list else False

    def hasNext(self) -> bool:
        return True if self.nodes_list else False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()