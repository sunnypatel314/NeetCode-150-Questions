from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackTemp, stackIndex = stack.pop()
                res[stackIndex] = i - stackIndex
            stack.append([t, i])
            
        return res

solution = Solution()

print(solution.dailyTemperatures(temperatures = [30,38,30,36,35,40,28])) # [1,4,1,2,1,0,0]
print(solution.dailyTemperatures(temperatures = [22,21,20])) # [0, 0, 0]