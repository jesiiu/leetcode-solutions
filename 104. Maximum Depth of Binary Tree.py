# 104. Maximum Depth of Binary Tree
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0

        if root.left == None and root.right == None:
            return 1

        leftDepth = self.maxDepth(root.left) if self.left else 0
        rigthDepth = self.maxDepth(root.right) if self.right else 0
        return max(leftDepth, rigthDepth) + 1
