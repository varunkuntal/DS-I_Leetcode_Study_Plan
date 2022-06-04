# Problem URL: https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k %= length

        p = 0
        temp = nums[(p+k)%length]
        nums[(p+k)%length] = nums[p]
        i = 0

        while i < length:
            p = (p+k)%length
            nums[(p+k)%length], temp = temp, nums[(p+k)%length]
            i += 1
        
        # # Naive Solution: O(n), O(n)
        # length = len(nums)
        # k = k % length
        # nums[:] = nums[length-k:] + nums[:length-k]
