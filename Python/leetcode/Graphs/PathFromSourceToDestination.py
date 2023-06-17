'''
This function gives a start and an end and returns the path to reach between the 2 nodes
'''

class Solution:

    def printDFS(self, n, edges, start, end): 

        graph = {i: [] for i in range(n)}
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        # print(graph)
    
        path = []
        def dfs(curr, currPath):
            if curr in visited:
                return
            if curr == end:
                currPath = currPath + [curr]
                path.extend(currPath)
                return
            currPath.append(curr)
            visited.add(curr)
            for n in graph[curr]:
                if n not in visited:
                    dfs(n, currPath)

        visited = set()
        dfs(start, [])
        return path
    
ob = Solution()
n = 5
edges = [
    [0,1],
    [1,4],
    # [2,3],
    # [3,4],
    [2,4]
]
path = ob.printDFS(n, edges, 4, 3)
print(path)