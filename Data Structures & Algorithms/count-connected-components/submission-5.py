class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adjlist, visited, count = defaultdict(list), [0] * n, 0

        for u, v in edges:
            adjlist[u].append(v)
            adjlist[v].append(u)

        def dfs(course):
            visited[course] = 1
            for neighbour in adjlist[course]:
                if visited[neighbour] == 0:
                    dfs(neighbour)
        
        for course in range(n):
            if visited[course] == 0:
                count += 1
                dfs(course)
        
        return count