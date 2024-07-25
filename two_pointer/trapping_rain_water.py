from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0

        left, right = 0, len(height) - 1
        max_left, max_right = height[left], height[right]

        total_water = 0

        while left < right:
            if max_left <= max_right:
                left += 1
                max_left = max(max_left, height[left])
                water = max_left - height[left]
                if water > 0:
                    total_water += water
            else:
                right -= 1
                max_right = max(max_right, height[right])
                water = max_right - height[right]
                if water > 0:
                    total_water += water

        return total_water

solution = Solution()

print(solution.trap(height = [0,2,0,3,1,0,1,3,2,1])) # 9