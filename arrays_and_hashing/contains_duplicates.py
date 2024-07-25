from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return (len(set(nums)) != len(nums))
    
solution = Solution()
print(solution.hasDuplicate(nums = [1, 2, 3, 3])) # True
print(solution.hasDuplicate(nums = [1, 2, 3, 4])) # False
    