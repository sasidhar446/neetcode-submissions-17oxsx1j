class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)
        visit = [0] * numCourses
        order = []

        for course, prereq in prerequisites:
            adjList[prereq].append(course)
        
        def hasCycle(course):
            if visit[course] == 1:
                return True
            if visit[course] == 2:
                return False

            visit[course] = 1

            for neighbour in adjList[course]:
                if hasCycle(neighbour):
                    return True
            
            order.append(course)
            visit[course] = 2

            return False

        for course in range(numCourses):
            if hasCycle(course):
                return []
        
        return order[::-1]
        