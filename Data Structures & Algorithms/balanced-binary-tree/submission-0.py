# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        max_height = 0

        def dfs(curr):
            if not curr:
                return 0
            else:
                left = dfs(curr.left)
                right = dfs(curr.right)
                nonlocal max_height
                max_height = max(max_height, abs(left - right))
                return max(left, right) + 1
        
        dfs(root)
        print(max_height)
        return True if max_height <= 1 else False



        