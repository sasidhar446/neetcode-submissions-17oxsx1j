# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        deq = collections.deque()
        deq.append(root)

        while deq:
            level = []
            deqLen = len(deq)
            for i in range(deqLen):
                node = deq.popleft()
                if node:
                    value, left, right = node.val, node.left, node.right
                    level.append(node.val)
                    if left:
                        deq.append(left)
                    if right:
                        deq.append(right)
            if level:
                result.append(level[-1])
        
        return result

        