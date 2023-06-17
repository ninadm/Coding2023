'''
Problem statement:

You are given a grid of cells, each containing a positive integer. Your task is to find a path from the top-left cell to the bottom-right cell, moving only downwards or rightwards, such that the sum of the numbers along the path is maximized.

You can only move to adjacent cells that are either to the right or below the current cell. You cannot move diagonally or move to cells that are outside the grid.

Write a backtracking algorithm to solve this problem and return the maximum sum achievable.

Function signature: `def max_path_sum(grid: List[List[int]]) -> int:`

Input:
- `grid`: A 2D grid of positive integers. The grid is represented as a list of lists, where each inner list represents a row in the grid. The length of each inner list will be the same, forming a rectangular grid.

Output:
- Return an integer representing the maximum sum achievable by following a path from the top-left cell to the bottom-right cell.

Note:
- It is guaranteed that the grid will have at least one cell.
- The grid will contain positive integers only.

Example:
```
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
output = max_path_sum(grid)
# Expected output: 1 + 4 + 7 + 8 + 9 = 29
```

Bakctracking Solution template
path that i can't take further
path that has provided a possible solution
path that I can take
'''

class Solution:
    def maxSumGrid(self, grid):

        def dfs(i, j, currSum):
            nonlocal ans
            # path I can't keep taking
            if i > len(grid) or j > len(grid[0]) or (i,j) in visited:
                return
            # path when a solution has reached
            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                ans = max(ans, currSum + grid[i][j])
            # I can keep continuing down this road
            currSum += grid[i][j]
            visited.add((i,j))
            if i < len(grid) - 1:
                dfs(i+1, j, currSum)
            if j < len(grid[0]) - 1:
                dfs(i, j+1, currSum)
            visited.remove((i,j))
            
        visited = set()
        ans = -1
        dfs(0, 0, 0)
        return ans
obj = Solution()
grid = grid = [    [1, 1, 1, 1],
    [1, 9, 1, 1],
    [1, 1, 1, 1]
]

print(obj.maxSumGrid(grid))



