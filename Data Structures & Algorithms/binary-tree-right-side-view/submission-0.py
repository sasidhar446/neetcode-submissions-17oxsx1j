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
            qLen = len(deq)
            level = []
            for i in range(qLen):
                node = deq.popleft()
                if node:
                    level.append(node.val)
                    deq.append(node.left)
                    deq.append(node.right)
            if level:
                result.append(level[-1])
            
        return result

        