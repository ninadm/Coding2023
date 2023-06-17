'''
Given a variable weight to reach a vertex from another vertex and a starting point, 
return a list of all vertices that can be reached from this one
'''

class Solution:

    def printDFS(self, n, edges, start, thresh):

        graph = {i: [] for i in range(n)}
        for edge in edges:
            graph[edge[0]].append([edge[1], edge[2]])
            graph[edge[1]].append([edge[0], edge[2]])

        def dfs(curr, currCost):
            if curr in visited:
                return
            if currCost <= thresh:
                visited.add(curr)
                for n in graph[curr]:
                    if n[0] not in visited and currCost + n[1] <= thresh:
                        dfs(n[0], currCost + n[1])

        
        visited = set()
        dfs(start, 0)
        return visited

ob = Solution()
n = 4
edges = [
    [0,1,1],
    [1,2,2],
    [0,3,1],
    [3,2,5]
]
ans = ob.printDFS(n, edges, 0, 2)
print(ans)
    