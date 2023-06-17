'''
3.
DFS that only prints from all vertices
'''
class Solution:

    def printDFS(self, n, edges): 

        graph = {i: [] for i in range(n)}
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
    

        def dfs(i, visited):
            if i in visited:
                print('_____')
                return 
            visited.append(i)
            
            for n in graph[i]:
                if n not in visited:
                    dfs(n, visited)

        for i in range(n):
            visited =  []
            dfs(i, visited)
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