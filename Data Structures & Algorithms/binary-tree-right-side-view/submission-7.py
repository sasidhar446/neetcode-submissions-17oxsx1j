# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        deq = collections.deque()
        deq.append(root)
        result = []

        while deq:
            deqLen = len(deq)
            level = []
            for _ in range(deqLen):
                node = deq.popleft()
                if node:
                    deq.append(node.left)
                    deq.append(node.right)
                    level.append(node.val)
            if level:
                result.append(level[-1])
        
        return result

        