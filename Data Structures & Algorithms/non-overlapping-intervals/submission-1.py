class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        newInterval, count = intervals[0], 0

        for start, end in intervals[1:]:
            lastEnd = newInterval[1]

            if start < lastEnd:
                count += 1
                newInterval[1] = min(lastEnd, end)
            else:
                newInterval = [start, end]
        
        return count


        