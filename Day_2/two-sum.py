# Problem URL: https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d = {}
        for k, i in enumerate(nums):
            comp = target - i
            if d.get(comp):
                return [d[comp]-1, k]
            else:
                d[i] = k+1

                
#         n = len(nums)
        
#         for i in range(n):
#             for j in range(i+1, n):
#                 if nums[i] + nums[j] == target:
#                     return [i,j]