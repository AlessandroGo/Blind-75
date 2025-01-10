class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # O(n) space with time O(amount*len(coins))
        dp = [amount+1] * (amount + 1)
        dp[0] = 0
        for a in range(1, amount+1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a-c])
        return dp[amount] if dp[amount] != amount + 1 else -1
    
obj1 = Solution()
coins = [1,2,5]
print(obj1.coinChange(coins, 11))
