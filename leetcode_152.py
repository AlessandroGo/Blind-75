class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(n^2)
        # maximum = nums[0]
        # for i in range(len(nums)):
        #     subArray = 1
        #     for j in range(i, len(nums)):
        #         subArray *= nums[j]
        #         if subArray > maximum:
        #             maximum = subArray
        # return maximum
        res = max(nums)
        curMin, curMax = 1, 1
        for n in nums:
            if n == 0:
                curMin, curMax = 1,1
                continue
            tmpCurMax = curMax * n
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(tmpCurMax, n*curMin, n) 
            res = max(res, curMax, curMin)
        return res
    
if __name__ == '__main__':
    nums = [-2,4,5,9]
    ob1 = Solution()
    print(ob1.maxProduct(nums))