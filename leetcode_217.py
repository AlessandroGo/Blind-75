class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # O(n) time but also O(n) space
        hashset = set()

        for n in nums: 
            if n in hashset:
                return True
            hashset.add(n)
        return False