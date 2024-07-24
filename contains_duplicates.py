from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return (len(set(nums)) != len(nums))
    
solution = Solution()

solution.hasDuplicate([1, 2, 3, 3]) # True
solution.hasDuplicate([1, 2, 3, 4]) # False
    