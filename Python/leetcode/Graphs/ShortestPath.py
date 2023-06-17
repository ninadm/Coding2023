'''
Given start and end, return the shortest path cost between them, weight of each edge will be unique
'''
import sys
class Solution:

    def printDFS(self, n, edges, start, end):

        graph = {i: [] for i in range(n)}
        for edge in edges:
            graph[edge[0]].append([edge[1], edge[2]])
            graph[edge[1]].append([edge[0], edge[2]])

        ans = sys.maxsize
        def dfs(curr, weight):
            nonlocal ans
            if weight >= ans:
                return
            if curr == end:
                ans = min(weight, ans)
                return
            visited.add(curr)
            for n in graph[curr]:
                if n[0] not in visited:
                    dfs(n[0], weight + n[1])
            visited.remove(curr)

        visited = set()
        
        dfs(start, 0)
        return ans

ob = Solution()
n = 4
edges = [
    [0,1,1],
    [1,2,0],
    [0,3,1],
    [3,2,1]
]
ans2 = ob.printDFS(n, edges, 0, 2)
print(ans2)


