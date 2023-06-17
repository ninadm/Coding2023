'''
5. Prints the total number of components or disjoint sets
'''
class Solution:

    def printDFS(self, n, edges): 

        graph = {i: [] for i in range(n)}
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        def dfs(curr):
            if curr in visited:
                return
            visited.add(curr)
            for ne in graph[curr]:
                if ne not in visited:
                    dfs(ne)


        components = 0
        visited = set()
        for i in range(n):
            if i not in visited:
                dfs(i)
                components += 1
        return components

ob = Solution()
n = 5
edges = [
    # [0,1],
    # [1,2],
    # [2,3],
    # [3,4],
    # [2,4]
]
components = ob.printDFS(n, edges)
print(components)
