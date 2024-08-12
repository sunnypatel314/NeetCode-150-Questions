from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (r + l) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid
        return -1

solution = Solution()

print(solution.search(nums = [-1,0,2,4,6,8], target = 4)) # 3
print(solution.search(nums = [-1,0,2,4,6,8], target = 3)) # -1