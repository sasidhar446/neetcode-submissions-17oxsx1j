class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(int)
        result = []
        for num in nums:
            frequency[num] += 1
        order = [[] for num in range(len(nums) + 1)]
        for k1, v in frequency.items():
            order[v].append(k1)
        for ord in order[::-1]:
            for x in ord:
                result.append(x)
                if len(result) == k:
                    return result
        return


        