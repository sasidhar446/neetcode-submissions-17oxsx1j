# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.max_height = 0

        def dfs(node):
            if not node:
                return 0
            else:
                left = dfs(node.left)
                right = dfs(node.right)

                self.max_height = max(self.max_height, abs(left - right))

                return max(left, right) + 1
        
        dfs(root)

        return True if self.max_height <= 1 else False
        

        

        