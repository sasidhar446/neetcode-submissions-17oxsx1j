class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = defaultdict(int)
        for num in nums:
            frequencies[num] += 1
        lookup = [[] for num in range(len(nums) + 1)]
        result = []
        for key, value in frequencies.items():
            lookup[value].append(key)
        # print(lookup)
        for i in range(len(lookup) -1, -1, -1):
            for ele in lookup[i]:
                result.append(ele)
                if len(result) == k:
                    return result
        return

