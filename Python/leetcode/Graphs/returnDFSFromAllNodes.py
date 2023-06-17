'''
4.
No need for this, we only need to simply just capture the visited list created in 3 in a separate array of arrays, that should print all paths
'''
class Solution:

    def printDFS(self, n, edges): 

        graph = {i: [] for i in range(n)}
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        

