class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = 0
        last_seen_fleet = -1
        cars = sorted(zip(position, speed), reverse=True)
        for p, s in cars:
            time_ = (target - p) / s
            if time_ > last_seen_fleet:
                fleet += 1
                last_seen_fleet = time_
        return fleet

        