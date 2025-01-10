class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(n^2) but there is an O(nlog(n))
        LIS = [1] * len(nums)
        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1+LIS[j])
        return max(LIS)

obj1 = Solution()
nums = [10,9,2,5,3,7,101,18]
print(obj1.lengthOfLIS(nums))