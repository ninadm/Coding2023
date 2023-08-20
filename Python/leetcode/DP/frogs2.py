'''
https://atcoder.jp/contests/dp/tasks/dp_b

10
0

20 10 (k = 1)
10    0
10    0

40 20 10 (k=1)
30 10  0

35 40 20 10 k = 2
   30 10  0
'''

def frogs2(input, k):
    dp = [0 for i in range(len(input))]
    for i in range(len(input) - 2, -1, -1):
        minimum_cost_k_steps = min(dp[i+1:min(len(dp),i+k+1)])
        index_of_minimum = dp[i+1:min(len(dp),i+k+1)].index(minimum_cost_k_steps) + i + 1
        dp[i] = minimum_cost_k_steps + abs(input[i] - input[index_of_minimum]) 
    return dp[0]

print(frogs2([10,30,40,50,20], 3))
print(frogs2([40,10,20,70,80,10,20,70,80,60], 4))
print(frogs2([10,20,10],1))
print(frogs2([10,10],100))


        

