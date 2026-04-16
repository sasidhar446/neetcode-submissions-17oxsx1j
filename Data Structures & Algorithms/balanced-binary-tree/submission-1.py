# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        result = 0
        def dfs(curr):
            if not curr:
                return 0
            else:
                nonlocal result
                left = dfs(curr.left)
                right = dfs(curr.right)
                result = max(result, abs(left - right))
                return max(left, right) + 1
        dfs(root)
        return False if result > 1 else True


        