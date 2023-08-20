'''
https://atcoder.jp/contests/dp/tasks/dp_a
10
0

30 10
20  0

60 30 10
   20   0


'''

def frogJumps(input):
    if len(input) == 1:
        return 0
    dp = [0 for i in range(len(input))]
    dp[-2] = abs(input[-1] - input[-2])
    for i in range(len(input)-3, -1, -1):
        dp[i] = min((abs(input[i] - input[i+1]) + dp[i+1]), (abs(input[i] - input[i+2]) + dp[i+2]))
    return dp[0]

print(frogJumps([10,30,40,20]))
print(frogJumps([10,10]))
print(frogJumps([30,10,60,10,60,50]))
