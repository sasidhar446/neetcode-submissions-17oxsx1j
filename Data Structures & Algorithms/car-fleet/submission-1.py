class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = []
        sorted_position = sorted(position, reverse=True)
        times = [(target - position_) / speed[position.index(position_)] for position_ in sorted_position]
        for time_ in times:
            if fleets and fleets[-1] >= time_:
                continue
            else:
                fleets.append(time_)
        return len(fleets)

        