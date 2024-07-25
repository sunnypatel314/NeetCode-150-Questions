from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 0
        s = set(nums)

        for i in nums:
            if i - 1 in s:
                continue
            current = 0
            while i in s:
                current += 1
                i += 1
            max_length = max(current, max_length)

            
        return max_length

solution = Solution()

print(solution.longestConsecutive(nums = [2,20,4,10,3,4,5])) # 4
print(solution.longestConsecutive(nums = [0,3,2,5,4,6,1,1])) # 7
      