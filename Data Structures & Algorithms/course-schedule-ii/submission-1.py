class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        visited, adjlist, order = [0] * numCourses, defaultdict(list), []

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
            order.append(course)
            
            return False
        
        for course in range(numCourses):
            if hasCycle(course):
                return []
        
        return order[::-1]
        