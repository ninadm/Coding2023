'''
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Input: nums = [0,1]
Output: [[0,1],[1,0]]

Input: nums = [1]
Output: [[1]]
'''
class Solution:
    def permutations(self, nums):
        res = []
        def backtrack(curr, arr):
            if len(arr) == 0:
                res.append(curr.copy())
                return
            for i in range(len(arr)):
                backtrack(curr + [arr[i]], arr[0:i]+ arr[i+1:])
        backtrack([], nums)
        return res

ob = Solution()
print(ob.permutations([1,2,3]))

    

