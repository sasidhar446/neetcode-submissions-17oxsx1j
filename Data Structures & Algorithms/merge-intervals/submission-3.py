class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        result = []
        result.append(intervals[0])

        for start, end in intervals[1:]:
            lastend = result[-1][1]

            if start <= lastend:
                result[-1][1] = max(lastend, end)
            else:
                result.append([start, end])
        
        return result
             


        