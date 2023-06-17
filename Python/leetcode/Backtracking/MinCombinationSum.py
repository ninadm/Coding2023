'''
Problem Statement:

Given a set of distinct integers and a target sum, your task is to find the minimum number of integers from the set that add up to the target sum. You can use each integer multiple times.

Write a backtracking algorithm to solve this problem and return the minimum number of integers required to achieve the target sum.

Function signature: def min_combinations(nums: List[int], target: int) -> int:
'''

import sys
class Solution:
    def minCombinationSum(self, nums, target):

        def dfs(currIdx, potentialSum):
            nonlocal minList
            nonlocal ans
            if currIdx >= len(nums) or sum(potentialSum) > target or len(potentialSum) > minList:
                return
            if sum(potentialSum) == target and len(potentialSum) < minList:
                ans = potentialSum.copy()
                minList = len(potentialSum)
                return
            
            potentialSum.append(nums[currIdx])
            dfs(currIdx, potentialSum)
            potentialSum.pop()
            dfs(currIdx+1, potentialSum)

        ans = []
        
        minList = sys.maxsize
        dfs(0, [])
        return ans

obj = Solution()
ans = obj.minCombinationSum([1,1,2], 1)
print(ans)
