class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        n = len(prices)
        profit = 0 
        for r in range(1,n): 
            if prices[l] < prices[r]:
                w = prices[r]-prices[l]
                profit = max(profit ,w)
            else:
                l=r
        return profit