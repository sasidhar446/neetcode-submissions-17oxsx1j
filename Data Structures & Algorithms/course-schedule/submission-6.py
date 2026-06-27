class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        visited, adj_list = [0] * numCourses, defaultdict(list)

        for v, u in prerequisites:
            adj_list[u].append(v)
        
        def hasCycle(course) -> bool:

            if visited[course] == 2:
                return False
            
            if visited[course] == 1:
                return True
            
            visited[course] = 1

            for neighbour in adj_list[course]:
                if hasCycle(neighbour):
                    return True

            visited[course] = 2

            return False

        
        for course in range(numCourses):
            if hasCycle(course):
                return False
        
        return True

