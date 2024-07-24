from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}

        for i in range(len(nums)):
            if target - nums[i] in mapping:
                return [mapping[target - nums[i]], i]

            mapping[nums[i]] = i

solution = Solution()

print(solution.twoSum(nums = [3,4,5,6], target = 7)) # [0, 1]
print(solution.twoSum(nums = [4,5,6], target = 10)) # [0, 2]
print(solution.twoSum(nums = [5,5], target = 10)) # [0, 1]
