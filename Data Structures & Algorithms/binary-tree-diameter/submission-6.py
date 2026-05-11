# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def dfs(root):
            if not root:
                return 0
            height1 = dfs(root.left)
            height2 = dfs(root.right)
            self.diameter = max(self.diameter, height1 + height2)
            return max(height1, height2) + 1

        dfs(root)
        
        return self.diameter


        

        
        