# Problem URL: https://leetcode.com/problems/reshape-the-matrix

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        p, q = len(mat), len(mat[0])
        
        elems = p * q
        
        t_elems = r * c
        
        if elems != t_elems:
            return mat
        
        m, n = 1, 1
        
        oned = []
        new = []
        temp = []
        
        for i in range(p):
            for j in range(q):
                oned.append(mat[i][j])
        
        k = 0
        
        for i in range(r):
            temp = []
            for j in range(c):
                
                temp.append(oned[k])
                k += 1
                
            new.append(temp)
        
        
        return new