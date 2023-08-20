'''
Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import defaultdict
from typing import List
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        '''
        Insights
        1. Can I think of this problem as a graph problem
            1.2 How do I turn a tree into a graph? Solved
        2. Let's first find the target node (duh, reference to the node is already given)
        3. Once I find the target node, I should then either use a dfs or a bfs to find the nodes at a distance of k
        '''
        parentMap = {}
        graph = defaultdict(list)
        def convertToGraph(curr):
            if not curr:
                return
            if curr in parentMap:
                graph[curr.val].append(parentMap[curr].val)
            if curr.left:
                graph[curr.val].append(curr.left.val)
                parentMap[curr.left] = curr
                convertToGraph(curr.left)
            if curr.right:
                graph[curr.val].append(curr.right.val)
                parentMap[curr.right] = curr
                convertToGraph(curr.right)
        convertToGraph(root)
        print(graph)


        visited = set()
        res = []
        def dfs(node, distance):
            if node in visited:
                return
            if distance == k:
                res.append(node)
                return
            visited.add(node)
            for nei in graph[node]:
                dfs(nei, distance + 1)
        
        dfs(target.val, 0)
        return res
