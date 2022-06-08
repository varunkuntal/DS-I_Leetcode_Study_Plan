# PROBLEM URL: https://leetcode.com/problems/pascals-triangle

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        f = []
        
        f.append([1])
        
        for i in range(1, numRows):
            f.append([1] * (i+1))
            for j in range(1, i):
                f[i][j] = f[i-1][j] + f[i-1][j-1]
                     
        return f
        