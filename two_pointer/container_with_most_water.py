from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        left, right = 0, len(heights) - 1

        while left < right:
            water_stored = min(heights[left], heights[right]) * (right - left)
            max_water = max(water_stored, max_water)

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        
        return max_water

solution = Solution()
print(solution.maxArea(heights = [1,7,2,5,4,7,3,6])) # 36
print(solution.maxArea(heights = [2,2,2])) # 4