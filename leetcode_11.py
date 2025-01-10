class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Brute force O(n^2) time 
        # res = 0
        # for left in range(len(height)):
        #     for right in range(left+1,range(len(height))):
        #         area = (right - left) * min(height[left], height[right])
        #         res = max(res, area)
        # return res
        
        # Linear time complexity
        # res = 0
        # l, r = 0, len(height) - 1

        # while l < r:
        #     area = (r-l)*min(height[l],height[r])
        #     res = max(res,area)
        #     if height[l] < height[r]:
        #         l += 1
        #     elif height[l] > height[r]:
        #         r -=1
        #     else:
        #         r -=1
        # return res

        # Similar using max
        l,r = 0, len(height)-1
        res = 0
        while l < r:
            if height[l] < height[r]:
                res = max(res, (r-l)*height[l])
                l += 1
            else:
                res = max(res, (r-l)*height[r])
                r -= 1
        return res
