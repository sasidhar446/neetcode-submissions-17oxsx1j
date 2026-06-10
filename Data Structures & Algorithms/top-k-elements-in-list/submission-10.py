class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = [[] for _ in range(len(nums) + 1)]
        lookup = defaultdict(int)
        result, count = [], 0

        for num in nums:
            lookup[num] += 1
        
        for key, value in lookup.items():
            frequencies[value].append(key)
        
        for i in range(len(frequencies) - 1, -1, -1):
            if frequencies[i]:
                for num in frequencies[i]:
                    result.append(num)
                    if len(result) == k:
                        return result
        
        return