# Problem URL: https://leetcode.com/problems/valid-sudoku

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        r, c = len(board), len(board[0])
        temp = {}
        
        for i in range(r):
            temp = {}
            for j in range(c):
                if board[i][j] != ".":
                    if temp.get(board[i][j]):
                        return False
                    else:
                        temp[board[i][j]] = 1
                    
        for i in range(r):
            temp = {}
            for j in range(c):
                if board[j][i] != ".":
                    if temp.get(board[j][i]):
                        return False
                    else:
                        temp[board[j][i]] = 1
                    
                    
        for i in [0,3,6]:
            for j in [0,3,6]:
                temp = {}
                for k in [0,1,2]:
                    for m in board[i:i+3][k][j:j+3]:
                        if m != ".":
                            if temp.get(m):
                                return False
                            else:
                                temp[m] = 1
                            
                            
        return True
                 