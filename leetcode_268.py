class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(n) time and space
        # hashMap = {}
        # for n in range(len(nums)):
        #     hashMap[n] = nums[n]
        # for n in range(len(nums) + 1):
        #     if n not in hashMap.values():
        #         return n

        # O(n)time O(1) space
        res = len(nums)
        for i in range(len(nums)):
            res += (i - nums[i])
        return res


       

nums1 = [3,0,1]
nums2 = [0,1]
nums3 = [9,6,4,2,3,5,7,0,1]
obj1 = Solution()
print(obj1.missingNumber(nums1))
print(obj1.missingNumber(nums2))
print(obj1.missingNumber(nums3))