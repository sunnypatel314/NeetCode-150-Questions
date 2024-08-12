from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def doesFinish(k):
            hours_left = h
            for p in piles:
                hours_left -= (p // k) + int(p % k > 0)
                if hours_left < 0:
                    return False
            return True

        left, right = 1, max(piles)
        res = right
        while left <= right:
            mid = (left + right) // 2
            if doesFinish(mid):
                res = min(res, mid)
                right = mid - 1
            else:
                left = mid + 1
        
        return res
    
solution = Solution()

print(solution.minEatingSpeed(piles = [1,4,3,2], h = 9)) # 2
print(solution.minEatingSpeed(piles = [25,10,23,4], h = 4)) # 25