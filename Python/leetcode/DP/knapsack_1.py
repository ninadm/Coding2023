'''
https://atcoder.jp/contests/dp/tasks/dp_d
Weight is 1 -> 1, 10
Weight is 2 -> max(1,10 OR 2,20)
weight is 3 -> dp[2] or do I have another weight that now becomes available to me? 
weight is 4 -> dp[3] NO

3,10
5,15
1,10
2,20
5,10

if I take 3 then I have 7 remaining and get a value of 10
if I take 5 then I have 5 remaining and get a value of 15

    0 1 2 3 4 5 6 7 8
0   0 0 0 0 0 0 0 0 0
1   0 
2   0
3   0
4   0
5   0


Dimensions of input for DP are the dimensions of the table


'''

n = 6
w = 15
input = [(6, 5), (5,6), (6, 4), (6, 6), (3, 5), (7, 2)]
def knapsack_1(n, w, input):
    dp = [[0] * (w+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1, w+1):
            current_item_weight = input[i-1][0]
            current_item_value = input[i-1][1]
            if current_item_weight <= j:  # Use <= instead of <
                dp[i][j] = max(dp[i-1][j], dp[i-1][j - current_item_weight] + current_item_value)
            else:
                dp[i][j] = dp[i-1][j]
    for i in range(len(dp)):
        print(dp[i])
    return dp[n][w]
                

    

print(knapsack_1(n,w,input))