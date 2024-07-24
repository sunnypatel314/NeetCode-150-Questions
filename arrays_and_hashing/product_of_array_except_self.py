from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        product_array = [1 for i in range(len(nums))]

        pre = 1
        for i in range(len(nums)):
            product_array[i] = pre
            pre *= nums[i]
        
        post = 1
        for i in range(len(nums) - 1, -1, -1):
            product_array[i] *= post
            post *= nums[i]
        
        return product_array
    
solution = Solution()

print(solution.productExceptSelf(nums = [1,2,4,6])) # [48, 24, 12, 8]
print(solution.productExceptSelf(nums = [-1,0,1,2,3])) # [0, -6, 0, 0, 0]


        
