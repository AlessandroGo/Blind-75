class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0 
        while n:
            # Make n%2 = 1 e.g. for 11 bin 1011 that last bit makes it odd if set 5 101 then 2 bin 10 see last bit not set so dont add bit to res 
            # then 1 bin 01 add res then 00
            res += n % 2
            n = n >> 1
        return res

    def hammingWeightBetter(self,n):
        res = 0
        while n:
            n = n & (n-1)
            res += 1
        return res
