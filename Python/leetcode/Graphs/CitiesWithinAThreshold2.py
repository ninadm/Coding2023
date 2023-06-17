'''
Given a threshold, 
return all vertices that can be reached from all vertices but within the threshold
'''

class Solution:

    def printDFS(self, n, edges, thresh):

        graph = {i: [] for i in range(n)}
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        # print(graph)

        def dfs(curr, pathLength):
            if curr in visited:
                return
            if pathLength <= thresh:
                visited.add(curr)
                for n in graph[curr]:
                    if n not in visited:
                        dfs(n, pathLength + 1)


        ans = {i: set() for i in range(n)}
        for i in range(n):
            visited = set()
            dfs(i, 0)
            visited.remove(i)
            ans[i].update(visited)
        return ans

ob = Solution()
n = 8
edges = [
    [0, 1],
    [0, 2],
    [1, 3],
    [1, 4],
    [2, 5],
    [2, 6],
    [3, 7],
    [4, 7],
    [5, 6],
    [6, 7]
]
ans = ob.printDFS(n, edges, 1)
print(ans)



        

