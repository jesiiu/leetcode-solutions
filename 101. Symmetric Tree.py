# 101. Symmetric Tree
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSymmetric(self, root):
        def isSymetricRecursive(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val != right.val:
                return False

            return isSymetricRecursive(left.left, right.right) and isSymetricRecursive(left.right, right.left)

        if not root:
            return True

        return isSymetricRecursive(root.left, root.right)
