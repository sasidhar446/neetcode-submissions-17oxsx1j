class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        output = [[] for i in range(len(nums) + 1)]
        result = []
        for num in nums:
            count[num] += 1
        for key, value in count.items():
            output[value].append(key)
        for i in range(len(output) - 1, 0, -1):
            for n in output[i]:
                result.append(n)
                if len(result) == k:
                    return result
            
        

        