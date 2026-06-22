class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        result, current = [], []

        def backtrack(index, remaining_target):
            if remaining_target == 0:
                result.append(current[:])
                return
            
            if remaining_target < 0:
                return
            
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                current.append(candidates[i])
                backtrack(i + 1, remaining_target - candidates[i])
                current.pop()
            
        backtrack(0, target)

        return result
            