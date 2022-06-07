class Solution:
    def maxProfit(self, prices: List[int]) -> int:

            maxprofit = 0
            minprice = float('inf')
        
            for i, j in enumerate(prices):
                if j < minprice:
                    minprice = j
                elif j - minprice > maxprofit:
                    maxprofit =  j - minprice   
                    
            return maxprofit
        