# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        curr, self.depth = root, 0

        def dfs(node, current_depth):
            if not node:
                return 0
            
            self.depth = max(self.depth, current_depth)

            dfs(node.left, current_depth + 1)
            dfs(node.right, current_depth + 1)

            return self.depth + 1
        
        return dfs(root, 0) 

  