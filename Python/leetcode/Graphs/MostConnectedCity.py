'''
Given a threshold, return a city such that it is connected to the most number of cities that lie within the threshold
'''

class Solution:

    def printDFS(self, n, edges, thresh):

        graph = {i: [] for i in range(n)}
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])


        def dfs(curr, currLength):
            if curr in visited:
                return
            if currLength <= thresh:
                visited.add(curr)
                for i in graph[curr]:
                    if i not in visited:
                        dfs(i, currLength + 1)

        highestScore = -1
        winningIndex = -1
        for i in range(n):
            visited = set()
            dfs(i, 0)
            if len(visited) > highestScore:
                winningIndex = i
                highestScore = len(visited)
        return winningIndex

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
