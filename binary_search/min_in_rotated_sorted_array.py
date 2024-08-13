from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        res = nums[0]
        
        while left <= right:
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break
            mid = (left + right) // 2
            res = min(res, nums[mid])
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1
        return res

solution = Solution()

print(solution.findMin(nums = [3,4,5,6,1,2])) # 1
print(solution.findMin(nums = [4,5,0,1,2,3])) # 0



