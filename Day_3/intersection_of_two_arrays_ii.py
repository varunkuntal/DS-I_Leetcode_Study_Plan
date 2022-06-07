# Problem URL: https://leetcode.com/problems/intersection-of-two-arrays-ii

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # TC: O(m * n) - m: No. of elements in nums1, n: No. of unique elements in nums1, SC O(n)
        rep = []
        
        f = {x:nums1.count(x) for x in set(nums1)}
        g = {x:nums2.count(x) for x in set(nums2)}
        
        
        for i in list(f.keys()):
            if g.get(i):
                rep.extend([i] * min(f[i], g[i]))
                del(f[i])
                del(g[i])
                
        return rep