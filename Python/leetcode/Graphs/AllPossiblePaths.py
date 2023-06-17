'''
Given start and end, return all possible unique paths between them
'''
class Solution:

    def printDFS(self, n, edges, start):
        graph = {i: [] for i in range(n)}
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        def dfs(curr, path):
            if curr == len(graph) - 1:
                ans.append(path + [curr])
                return
            visited.add(curr)
            for neighbor in graph[curr]:
                if neighbor not in visited:
                    dfs(neighbor, path + [curr])
            visited.remove(curr)
        
        ans = []
        visited = set()
        dfs(start, [])
        return ans

    
ob = Solution()
n = 4
edges = [
    [0,1],
    [1,2],
    [0,3],
    [3,2]
]
ans = ob.printDFS(n, edges, 0, 2)
print(ans)