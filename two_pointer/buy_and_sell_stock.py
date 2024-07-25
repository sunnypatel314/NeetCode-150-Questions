from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        minimum_price = prices[0]

        for p in prices:
            profit = p - minimum_price
            minimum_price = min(p, minimum_price)
            max_profit = max(profit, max_profit)

        return max_profit

solution = Solution()

print(solution.maxProfit(prices = [10,1,5,6,7,1])) # 6
print(solution.maxProfit(prices = [10,8,7,5,2])) # 0