# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        result = True

        def dfs(root):
            nonlocal result
            if not root:
                return 0
            left_height = dfs(root.left)
            right_height = dfs(root.right)
            result = False if abs(left_height - right_height) > 1 else True and result
            return max(left_height, right_height) + 1

        dfs(root)

        return result
        





        