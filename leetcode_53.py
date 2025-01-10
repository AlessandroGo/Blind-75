class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(n^2) time and O(1) space
        n, res = len(nums), nums[0]
        for i in range(n):
            cur = 0
            for j in range(i, n):
                cur += nums[j]
                res = max(res, cur)
        return res

        # Using Kadanes algorithm O(n) and space O(1)
        # maxSub, curSum = nums[0], 0
        # for num in nums:
        #     if curSum < 0:
        #         curSum = 0
        #     curSum += num 
        #     maxSub = max(maxSub, curSum)
        # return maxSub

def main():
    input = [5,4,-1,7,8] # [-2,1,-3,4,-1,2,1,-5,4]
    obj1 = Solution()
    output = obj1.maxSubArray(input)
    print(output)

main()