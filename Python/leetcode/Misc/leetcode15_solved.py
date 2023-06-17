'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
what if I was to sort
-4, -1, -1, 0, 1, 2
I do think we can do this simply with the help of sorting and two pointers.
the complexity will be o(nlogn)
'''

class Solution:
    def allZeroTriplets(self, nums):
        ans = []
        nums.sort()
        print(nums)


        
        for i in range(len(nums) - 2):
            print('here')
            j = i+1
            k = len(nums) - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while j < k:
                if nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
        return ans

ob = Solution()
print(ob.allZeroTriplets([-1,0,1,2,-1,-4]))