class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        visited, adjlist = [0] * numCourses, defaultdict(list)

        for u, v in prerequisites:
            adjlist[v].append(u)
        
        def hasCycle(course) -> bool:
            if visited[course] == 1:
                return True
            if visited[course] == 2:
                return False
            
            visited[course] = 1

            for neighbour in adjlist[course]:
                if hasCycle(neighbour):
                    return True
            
            visited[course] = 2

            return False
        
        for course in range(numCourses):
            if visited[course] == 0:
                if hasCycle(course):
                    return False
        
        return True
