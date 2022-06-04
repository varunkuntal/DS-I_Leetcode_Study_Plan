# Problem URL: https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        
        # Approach 1
        # O(n), O(n)
        d = {}
        for i in nums:
            if d.get(i):
                return True
            else:
                d[i] = 1
        return False
        
        # # Approach 2
        # # O(nlogn), O(1)
        # nums.sort()
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i-1]:
        #         return True
        # return False
        
        # # Approach 3
        # # O(n), O(n)
        # return len(set(nums)) != len(nums)