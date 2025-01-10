class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res , sol = [], [] # sol is interim list
        nums = candidates
        n = len(nums)

        def backtrack(i,cur_sum):
            if cur_sum == target:
                res.append(sol[:])
                return
            if cur_sum > target or i == n: # if over target or at end of list
                return
            
            backtrack(i+1, cur_sum)
            sol.append(nums[i])
            backtrack(i, cur_sum + nums[i])
            sol.pop()
        
        backtrack(0,0)
        return res
    # Time complexity is O(N^(T/M+1)) where T is the target value and M is the minimal value among the candidates

if __name__ == '__main__':
    obj1 = Solution()
    candidates = [2,3,5]
    print(obj1.combinationSum(candidates, 8))