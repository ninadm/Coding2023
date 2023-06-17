'''
This function gives a start and an end and returns true or false based on if there exists a path from start to end
'''

class Solution:

    def printDFS(self, n, edges, start, end): 

        graph = {i: [] for i in range(n)}
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        

        def dfs(curr):
            if curr in visited:
                return
            if curr == end:
                return True
            visited.add(curr)
            for n in graph[curr]:
                if n not in visited:
                    if dfs(n):
                        return True
            return False

        visited = set()
        return dfs(start)

ob = Solution()
n = 5
edges = [
    [0,1],
    # [1,2],
    [2,3],
    [3,4],
    [2,4]
]
canReach = ob.printDFS(n, edges, 0, 4)
print(canReach)

        