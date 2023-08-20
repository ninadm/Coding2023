'''
https://atcoder.jp/contests/dp/tasks/dp_c
input = [[100,5,5], [10,3,4]]
100
10

5
3

5
4

100 5 5
104 15 15
days = 2
answer is 104
'''

def vacation(input):
    dp = [[0 for _ in range(3)] for _ in range(len(input))]
    dp[0] = input[0]
    
    for i in range(1, len(input)):
        
        dp[i][0] = input[i][0] + max(dp[i-1][1], dp[i-1][2])
        dp[i][1] = input[i][1] + max(dp[i-1][0], dp[i-1][2])
        dp[i][2] = input[i][2] + max(dp[i-1][0], dp[i-1][1])
    print(dp)
    return max(dp[-1])

print(vacation([[10,40,70], [20,50,80], [30,60,90]]))
print(vacation([[100,10,1]]))
print(vacation([[6,7,8], [8,8,3], [2,5,2], [7,8,6], [4,6,8], [2,3,4], [7,5,1]]))