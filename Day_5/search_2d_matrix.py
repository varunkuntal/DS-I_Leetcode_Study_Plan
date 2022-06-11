# Problem URL: https://leetcode.com/problems/search-a-2d-matrix

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def bs(arr, n):
            s = 0
            e = len(arr)-1
            while s <= e:
                mid = (s + e) // 2
                if arr[mid] > n:
                    e = mid - 1
                elif arr[mid] < n:
                    s = mid + 1
                else:
                    return mid
            return -1, mid
        
        
        a,b = len(matrix), len(matrix[0])

        if target < matrix[0][0] or target > matrix[a-1][b-1]:
            return False
        
        firstcolumn = [i[0] for i in matrix]
        
        res = bs(firstcolumn, target)

        
        if isinstance(res, int):
            return True
        else:
            if firstcolumn[res[1]] > target:
                idx = res[1] - 1
            else:
                idx = res[1]
                
            if firstcolumn[res[1]] > target:
                idx = res[1] - 1
            else:
                idx = res[1]
                
            res = bs(matrix[idx], target)
            
            if isinstance(res, int):
                return True
            return False
        
# ---------------------------------------------------------------     
#        # Brute Force O(n^2)
#         a,b = len(matrix), len(matrix[0])
#         for i in range(a):
#             for j in range(b):
#                 if matrix[i][j] == target:
#                     return True

#         return False
# ---------------------------------------------------------------
        # # Pythonic One-Liner O(n^2) Brute Force
        # return any(target in row for row in matrix)

            