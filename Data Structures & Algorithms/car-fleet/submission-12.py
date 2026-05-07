class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        time = []
        for pos, speed in sorted(zip(position, speed), reverse = True):
            time.append((target - pos) / speed)
        count, max_ele = 1, time[0]
        for i in range(1, len(time)):
            if time[i] > max_ele:
                max_ele = time[i]
                count += 1
        return count
        
            



            