class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time_, fleets, max_ = [], 0, 0
        for p, s in sorted(zip(position, speed), reverse = True):
            time_.append((target - p) / s)
        for i in time_:
            if max_ < i:
                fleets += 1
                max_ = i
        return fleets
        
            



            