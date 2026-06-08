# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        curr, self.good_nodes = root, 0

        def dfs(curr, max_val):
            if not curr:
                return
            if curr.val >= max_val:
                self.good_nodes += 1
            dfs(curr.left, max(curr.val, max_val))
            dfs(curr.right, max(curr.val, max_val))
        
        dfs(curr, float("-inf"))

        return self.good_nodes







        