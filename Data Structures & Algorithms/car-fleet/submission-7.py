class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        count = 0
        last_time = -1
        for pos, spe in sorted(zip(position, speed), reverse = True):
            time_ = (target - pos) / spe
            if time_ > last_time:
                count += 1
                last_time = time_
        return count