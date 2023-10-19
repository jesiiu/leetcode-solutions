# 110. Balanced Binary Tree
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isBalanced(self, root):
        if root is None:
            return True

        def get_height(node):
            if node is None:
                return 0

            left_heigh = get_height(node.left)
            if left_heigh == -1:
                return -1
            right_heigh = get_height(node.right)
            if right_heigh == -1:
                return -1
            if abs(left_heigh - right_heigh) > 1:
                return -1
            return 1 + max(left_heigh, right_heigh)

        return get_height(root) != -1
