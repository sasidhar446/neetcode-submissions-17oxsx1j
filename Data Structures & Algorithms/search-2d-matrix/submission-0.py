class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        total = []
        for element in matrix:
            total += element
        left, right = 0, len(total) - 1
        while left <= right:
            middle = (left + right) // 2
            target_ = total[middle]
            if target_ == target:
                return True
            elif target_ > target:
                right = middle - 1
            else:
                left = middle+1
        return False