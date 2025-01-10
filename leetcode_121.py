class Solution(object):
    def maxProfit(self, prices) -> int:
        """
        :type prices: List[int]
        :rtype: int
        """
        l, r = 0, 1 # Left buy right sell   
        maxP = 0
        while r < len(prices):
            # profit
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l += 1    
            r += 1    
        return maxP