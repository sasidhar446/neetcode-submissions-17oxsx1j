class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)

        def canReach(current: int, target: int, visited: set) -> bool:
            if current == target:
                return True
            
            visited.add(current)

            for neighbour in adjList[current]:
                if neighbour not in visited:
                    if canReach(neighbour, target, visited):
                        return True
            
            return False


        for k, v in edges:
            if canReach(k, v, set()):
                return [k, v]
            
            adjList[k].append(v)
            adjList[v].append(k)
        
        return []