import unittest

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashMap = {} # Store val : index
        for i, n in enumerate(nums):
            difference = target - n
            if difference in hashMap:
                return [hashMap[difference], i]
            hashMap[n] = i


class TestSolution(unittest.TestCase):
    def test_target_9(self):
        nums = [2,7,11,15]
        object1 = Solution()
        output = object1.twoSum(nums, 9)
        self.assertEqual(output, [0,1])
    def test_target_6(self):
        nums = [3,2,4]
        object1 = Solution()
        output = object1.twoSum(nums, 6)
        self.assertEqual(output, [1,2])

if __name__ == '__main__':
    unittest.main(verbosity=2)