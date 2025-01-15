class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        prereqMap = {i : [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            prereqMap[course].append(prereq)
        
        output = []
        visit, cycle = set(), set()
        def dfs(course):
            if course in cycle:
                return False
            if course in visit:
                return True
            cycle.add(course)
            for prereq in prereqMap[course]:
                if dfs(prereq) == False:
                    return False
            cycle.remove(course)
            visit.add(course)
            output.append(course)
            return True

        for course in range(numCourses):
            if dfs(course) == False :
                return []
        
        return output
        
if __name__ == '__main__':
    obj1 = Solution()
    print(obj1.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))