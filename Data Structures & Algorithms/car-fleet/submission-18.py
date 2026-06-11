class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        current_fleet, result = 0, 0
        for p, s in sorted(zip(position, speed), reverse=True):
            fleet = (target - p) / s
            if fleet > current_fleet:
                result += 1
                current_fleet = fleet
        
        return result


        
            



            