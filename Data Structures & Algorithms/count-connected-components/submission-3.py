class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = defaultdict(list)
        count = 0
        visit = [0] * n

        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])

        def dfs(node):
            if visit[node] == 1:
                return
            visit[node] = 1
            for neighbour in adjList[node]:
                dfs(neighbour)
        
        for node in range(n):
            if visit[node] == 0:
                count += 1
                dfs(node)
        
        return count
