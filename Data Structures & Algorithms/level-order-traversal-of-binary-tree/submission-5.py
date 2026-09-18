# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        deq = collections.deque()
        deq.append(root)
        result = []

        while deq:
            deqlen = len(deq)
            current = []
            for _ in range(deqlen):
                node = deq.popleft()
                if node:
                    current.append(node.val)
                    deq.append(node.left)
                    deq.append(node.right)
            if current:
                result.append(current)
        
        return result

                

        