from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        res = []
        freq = [[] for i in range(len(nums) + 1)]
        counter_nums = Counter(nums)

        for i in counter_nums.keys():
            freq[counter_nums[i]].append(i)
        for i in freq[::-1]:
            if k == 0:
                continue
            if len(i) == 0:
                continue
            for x in i:
                res.append(x)
                k -= 1
        
        return res

solution = Solution()

print(solution.topKFrequent(nums = [1,2,2,3,3,3], k = 2)) # [3, 2]
print(solution.topKFrequent(nums = [7,7], k = 1)) # [7]

            