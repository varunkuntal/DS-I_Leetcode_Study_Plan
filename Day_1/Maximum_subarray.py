# Problem URL: https://leetcode.com/problems/maximum-subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxArray = nums[0]
        currSum = 0
        
        for i in nums:
            if currSum < 0:
                currSum = 0
                
            currSum += i
                
            maxArray = max(currSum, maxArray)
            
        return maxArray
                
            
                    
                    
                    
        
#         # O(n^2) Optimized Brute Force
#         n = len(nums)
#         total = nums[0]
#         for i in range(n):
#             res = 0
#             for j in range(i, n):
#                 res += nums[j]
#                 if res > total:
#                     total = res
                
#         return total
        