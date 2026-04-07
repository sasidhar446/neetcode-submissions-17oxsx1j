class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)
        result = []
        counts = [[] for i in range(len(nums) + 1)]
        for num in nums:
            freq_map[num] += 1
        for num, count in freq_map.items():
            counts[count].append(num)
        for i in range(len(counts) -1, -1, -1):
            for j in counts[i]:
                result.append(j)
                if len(result) == k:
                    return result
        return result