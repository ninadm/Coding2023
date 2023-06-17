'''
A node is given as the start point, return all the edges we can reach from it.
'''

class Solution:

    def printDFS(self, n, edges, start): 

        graph = {i: [] for i in range(n)}
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        visited = set()
        def dfs(curr):
            if curr in visited:
                return
            visited.add(curr)
            for n in graph[curr]:
                if n not in visited:
                    dfs(n)
    
        dfs(start)
        visited.remove(start)
        return visited

ob = Solution()
n = 5
edges = [
    [0,1],
    # [1,2],
    [2,3],
    [3,4],
    [2,4]
]
visited = ob.printDFS(n, edges, 4)
print(visited)

