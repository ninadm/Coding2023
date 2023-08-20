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




'''