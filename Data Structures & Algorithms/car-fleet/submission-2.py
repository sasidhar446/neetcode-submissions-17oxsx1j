class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = []
        cars = sorted(zip(position, speed), reverse=True)
        for p, s in cars:
            time_ = (target - p) / s
            if fleets and fleets[-1] >= time_:
                continue
            else:
                fleets.append(time_)
        return len(fleets)

        