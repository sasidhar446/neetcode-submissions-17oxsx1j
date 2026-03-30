class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            result = numbers[i] + numbers[j]
            if result == target:
                return [i + 1, j + 1]
            elif result > target:
                j -= 1
            else:
                i += 1
        return
        