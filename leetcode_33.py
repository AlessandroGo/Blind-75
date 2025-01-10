class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l,r = 0, len(nums) - 1
        while l <= r:
            mid = (l+r)//2
            if target == nums[mid]:
                return mid
            # left sorted portion has middle value so nums[mid] > nums[l] as contiguous sections are sorted
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # Right sorted portion has middle value 
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return - 1

ob1 = Solution()
nums = [4,5,6,7,8,1,2]
print(ob1.search(nums, 8))