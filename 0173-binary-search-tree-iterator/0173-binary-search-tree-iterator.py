# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.nodes_lst = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            self.nodes_lst.append(root.val)
            inorder(root.right)
        inorder(root)

    def next(self) -> int:
        return self.nodes_lst.pop(0) if self.nodes_lst else False

    def hasNext(self) -> bool:
        return True if self.nodes_lst else False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()