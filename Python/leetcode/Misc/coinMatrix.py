'''
Coins are placed in a maze of dimensions r*c. Each element is the denomination. You can choose to go up down left or right. 
Only catch is that you may only go and select a coin, larger than the current denomination. 
Return the maximum money you can collect.



'''
import random

# Define the dimensions of the matrix
rows, columns = 10, 10

# Create a 10x10 matrix with random positive integers between 1 and 100
maze = [[random.randint(1, 100) for _ in range(columns)] for _ in range(rows)]
for row in maze:
    print(row)

def getMaximumProfit(maze):
    r,c = len(maze), len(maze[0])
    
    def inbound(i, j):
        return 0 <= i < r and 0 <= j < c
        
    def dfs(i, j, visited, memo={}):
        if (i, j) in memo:
            return memo[(i, j)]
        if 0 <= i < r and 0 <= j < c and (i, j) not in visited:
            visited.add((i, j))
            up, down, left, right = 0,0,0,0
            if inbound(i+1, j) and maze[i+1][j] >= maze[i][j]:
                down = maze[i][j] + dfs(i+1, j, visited, memo)
            if inbound(i-1, j) and maze[i-1][j] >= maze[i][j]:
                up = maze[i][j] + dfs(i-1, j, visited, memo)
            if inbound(i, j-1) and maze[i][j-1] >= maze[i][j]:
                left = maze[i][j] + dfs(i, j-1, visited, memo)
            if inbound(i, j+1) and maze[i][j+1] >= maze[i][j]:
                right = maze[i][j] + dfs(i, j+1, visited, memo)
            # print(left, right, up, down)
            memo[(i,j)] = max(up, down, left, right)
            return max(up, down, left, right)
        memo[(i,j)] = 0
        return 0


    ans = 0
    for i in range(r):
        for j in range(c):
            ans = max(ans, dfs(i, j, set()))
    return ans

print(getMaximumProfit(maze))
