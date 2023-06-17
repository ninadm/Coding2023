'''
Given a starting point and path length, 
return all vertices that can be reached from the starting point but within the limit
'''

class Solution:

    def printDFS(self, n, edges, start, thresh):

        graph = {i: [] for i in range(n)}
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        def dfs(curr, currLength):
            if curr in visited:
                return
            visited.add(curr)
            if currLength <= thresh:
                ans[start].add(curr)
            for n in graph[curr]:
                if n not in visited:
                    dfs(n, currLength + 1)
        
        ans = {start: set()}
        visited = set()
        dfs(start, 0)
        return ans

ob = Solution()
n = 5
edges = [
    [0,1],
    [1,2],
    [2,3],
    [3,4]
]
path = ob.printDFS(n, edges, 2, 2)
print(path)
        

