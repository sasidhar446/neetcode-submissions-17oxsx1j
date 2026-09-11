class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        positions = sorted(zip(position, speed), reverse=True)
        result, current_fleet = 0, 0
        time_left = []
        for p,s in positions:
            fleet = (target - p) / s
            if fleet > current_fleet:
                result += 1
                current_fleet = fleet
                
        return result


        
            



            