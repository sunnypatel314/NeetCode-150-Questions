from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bottom = 0, ROWS - 1
        while top <= bottom:
            row = (top + bottom) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break

        if top > bottom:
            return False
        row = (top + bottom) // 2

        left, right = 0, len(matrix[row])
        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] > target:
                right = mid - 1
            elif matrix[row][mid] < target:
                left = mid + 1
            else:
                return True
        return False


solution = Solution()

print(solution.searchMatrix(matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10)) # True
print(solution.searchMatrix(matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 15)) # False