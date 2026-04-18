# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root, new_max):
            if not root:
                return 0
            is_good = 1 if root.val >= new_max else 0
            new_max = max(root.val, new_max)

            return is_good + dfs(root.left, new_max) + dfs(root.right, new_max)

        return dfs(root, float("-inf"))




        