class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        preMap = {i : [] for i in range(numCourses)}
        for course , prereq in prerequisites:
            preMap[course].append(prereq)

        visitedSet = set()
        def dfs(course):
            if course in visitedSet:
                return False
            if preMap[course] == []:
                return True
            visitedSet.add(course)
            for prereq in preMap[course]:
                if not dfs(prereq) : return False
            visitedSet.remove(course)
            preMap[course] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course) : return False
            
        return True


obj1 = Solution()
print(obj1.canFinish(2, [[1,0],[0,1]]))

# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         indegree = [0] * numCourses
#         adj = [[] for x in range(numCourses)]
        
#         for prereq in prerequisites:
#             adj[prereq[1]].append(prereq[0])
#             indegree[prereq[0]] += 1

#         queue = []
#         for i in range(numCourses):
#             if indegree[i] == 0:
#                 queue.append(i)
        
#         visited = 0
#         while queue:
#             node = queue.pop(0)
#             visited += 1
#             for neighbor in adj[node]:
#                 indegree[neighbor] -= 1
#                 if indegree[neighbor] == 0:
#                     queue.append(neighbor)
        
#         return numCourses == visited