class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # res = []
        # # n times O(n)
        # for i in range(n+1):
        #     current_ones = 0
        #     # log(n) times as i /= 2 is log(n) times
        #     while i != 0:
        #         current_ones += i%2
        #         i /= 2
        #     res.append(current_ones)
        # return res

        # O(n) solution
        dp = [0] * (n+1)
        offset = 1

        for i in range(1, n+1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp