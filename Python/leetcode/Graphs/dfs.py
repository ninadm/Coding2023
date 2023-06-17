'''
1
This code prints the path taken by DFS in a undirected graph. 
It does not consider anything else like is the graph connected or not. 
If it isn't the dfs will simply stop in it's track
'''


class Solution:

    def printDFS(self, n, edges): 

        graph = {i: [] for i in range(n)}
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        visited = [] # usually take a set, but for printing better to take a list since the order is being maintained

        def dfs(curr):
            if curr in visited:
                return
            visited.append(curr)
            for neighbour in graph[curr]:
                if neighbour not in visited:
                    dfs(neighbour)

        
        dfs(0)
        print(visited)
    
ob = Solution()
n = 5
edges = [
    [0,1],
    [1,2],
    [2,3],
    [3,4],
    [2,4]
]
ob.printDFS(n, edges)
            
