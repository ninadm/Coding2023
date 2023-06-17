'''

Given an integer array nums that may contain duplicates, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:

Input: nums = [0]
Output: [[],[0]]

# should I consider using a set as my final result and
'''

class Solution:
    def powerSet(self, nums):
        res = []
        def backtrack(i, curr):
            if i >= len(nums):
                res.append(curr.copy())
                return
            curr.append(nums[i])
            backtrack(i+1, curr)
            curr.pop()
            backtrack(i+1, curr)
        backtrack(0, [])
        return res
ob = Solution()
print(ob.powerSet([1,2,3]))
        