# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = 0
        new_max = float("-inf")

        def dfs(root, new_max):
            nonlocal result
            if not root:
                return
            else:
                if root.val >= new_max:
                    result += 1
                dfs(root.left, max(new_max, root.val))
                dfs(root.right, max(new_max, root.val))
        
        dfs(root, new_max)

        return result




        