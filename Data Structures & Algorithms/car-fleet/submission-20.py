class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        positions = sorted(zip(position, speed), reverse=True)
        count = 1
        time_left = []
        for p,s in positions:
            time_left.append((target - p) / s)
        fleet = time_left[0]
        for ele in time_left:
            if ele > fleet:
                count += 1
                fleet = ele
        return count


        
            



            