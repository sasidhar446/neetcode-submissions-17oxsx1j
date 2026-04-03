class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        buckets = [[] for i in range(len(nums) + 1)]
        for key, value in counts.items():
            buckets[value].append(key)
        result = []
        for i in range(len(buckets) - 1, -1, -1):
            if buckets[i]:
                for num in buckets[i]:
                    result.append(num)
                    if len(result) == k:
                        return result
        return result