class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        visit = [0] * numCourses

        for course, prereq in prerequisites:
            adj_list[prereq].append(course)

        def has_cycle(course):
            if visit[course] == 1:
                return True
            if visit[course] == 2:
                return False
            
            visit[course] = 1

            for neighbour in adj_list[course]:
                if has_cycle(neighbour):
                    return True
            
            visit[course] = 2

            return False
        
        for course in range(numCourses):
            if has_cycle(course):
                return False
        
        return True

