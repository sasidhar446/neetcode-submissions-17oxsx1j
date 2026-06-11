class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = [0] * len(position)
        for index, result in enumerate(sorted(zip(position, speed), reverse=True)):
            fleets[index] = (target - result[0]) / result[1]
        
        count = 0
        current_fleet = 0
        
        for fleet in fleets:
            if fleet > current_fleet:
                count += 1
                current_fleet = fleet
        
        return count


        
            



            