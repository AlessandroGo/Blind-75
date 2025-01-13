class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        row = [1] * n
        for i in range(m -1):
            newRow = [1] * n
            for j in range(n-2,-1,-1):
                newRow[j] = newRow[j+1] + row[j] # Because row[j] is when it turns down and newRow[j+1] is turn right
            row = newRow
        return row[0]
        