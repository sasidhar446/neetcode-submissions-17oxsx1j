# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        result = 0

        def dfs(node):
            nonlocal result
            if not node:
                return 0
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            result = max(result, abs(left_height - right_height))
            return max(left_height, right_height) + 1

        dfs(root)

        return True if result <= 1 else False



        