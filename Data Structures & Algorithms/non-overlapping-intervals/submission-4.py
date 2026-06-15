class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])

        lastEnd, count = intervals[0][1], 0

        for start, end in intervals[1:]:

            if start < lastEnd:
                count += 1
            else:
                lastEnd = end
        
        return count


        