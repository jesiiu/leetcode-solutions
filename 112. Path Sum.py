#112. Path Sum
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def hasPathSum(self, root, targetSum):
        def bfs(node):
            if node is None:
                return False
            
            queue = [(node, 0)]
            
            while queue:
                cn, cs = queue.pop(0)
                cs += cn.val
                
                if not cn.left and not cn.right and cs == targetSum:
                    return True
                if cn.left is not None:
                    queue.append((cn.left, cs))
                if cn.right is not None:
                    queue.append((cn.right, cs))
            return False
        return bfs(root)
                    
        