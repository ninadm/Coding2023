'''
2
This code returns dfs. 
It does not consider anything else like is the graph connected or not. 
If it isn't the dfs will simply stop in it's track
'''
class Solution:

    def printDFS(self, n, edges): 

        graph = {i: [] for i in range(n)}
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        visited = set()

        def dfs(curr):
            if curr in visited:
                return
            visited.add(curr)
            for nei in graph[curr]:
                if nei not in visited:
                    dfs(nei)
        
        dfs(0)
        return visited

ob = Solution()
n = 5
edges = [
    [0,1],
    [1,2],
    [2,3],
    [3,4],
    [2,4]
]
visited = ob.printDFS(n, edges)
print(visited)
