class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []

        def dfs(i,cur,total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return

            cur.append(candidates[i])
            dfs(i,cur,total + candidates[i])
            cur.pop()
            dfs(i+1,cur,total)
        
        dfs(0, [], 0)
        return res
    
obj1 = Solution()
candidates = [2,3,6,7]
print(obj1.combinationSum(candidates, 7))