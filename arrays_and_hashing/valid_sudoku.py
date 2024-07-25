from typing import List
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            s = set()
            for x in board[i]:
                if x in s:
                    return False
                if x != ".":
                    s.add(x)

            s = set()
            for y in range(len(board[i])):
                if board[y][i] in s:
                    return False
                if board[y][i] != ".":
                    s.add(board[y][i])

        hm = defaultdict(list)
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                r, c = i // 3, j // 3
                if board[i][j] in hm[(r, c)]:
                    return False
                if board[i][j] != ".":
                    hm[(r, c)].append(board[i][j])
            
        return True 

solution = Solution()

print(solution.isValidSudoku(board = 
                            [
                                ["1","2",".",".","3",".",".",".","."],
                                ["4",".",".","5",".",".",".",".","."],
                                [".","9","8",".",".",".",".",".","3"],
                                ["5",".",".",".","6",".",".",".","4"],
                                [".",".",".","8",".","3",".",".","5"],
                                ["7",".",".",".","2",".",".",".","6"],
                                [".",".",".",".",".",".","2",".","."],
                                [".",".",".","4","1","9",".",".","8"],
                                [".",".",".",".","8",".",".","7","9"]
                            ])) # True
print(solution.isValidSudoku(board=
                             [
                                ["1","2",".",".","3",".",".",".","."],
                                ["4",".",".","5",".",".",".",".","."],
                                [".","9","1",".",".",".",".",".","3"],
                                ["5",".",".",".","6",".",".",".","4"],
                                [".",".",".","8",".","3",".",".","5"],
                                ["7",".",".",".","2",".",".",".","6"],
                                [".",".",".",".",".",".","2",".","."],
                                [".",".",".","4","1","9",".",".","8"],
                                [".",".",".",".","8",".",".","7","9"]
                             ])) # False
            

        