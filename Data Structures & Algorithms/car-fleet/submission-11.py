class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        time = []
        for pos, speed in sorted(zip(position, speed), reverse = True):
            time.append((target - pos) / speed)
        for ele in time:
            if not stack or stack[-1] < ele:
                stack.append(ele)
        return len(stack)
        
            



            