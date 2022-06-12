# Problem URL: https://leetcode.com/problems/first-unique-character-in-a-string

class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        d = {x:(s.count(x), s.index(x)) for x in set(s) if s.count(x) == 1}
        
        minidx = [0,float('inf')]
        for i in d:
            if minidx[1] > d[i][1]:
                minidx = [i, d[i][1]]
                
        if minidx[0] != 0:
            return minidx[1]
            
        return -1
        
        
        
