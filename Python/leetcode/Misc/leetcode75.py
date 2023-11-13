'''
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 

Example 1:

Input: nums = [2,0,2,1,1,0]


Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1] [102]
Output: [0,1,2]
 


'''
from collections import defaultdict
nums = [2,0,2,1,1,0]
def sortColors():
    mapp = defaultdict(int)
    for num in nums:
        mapp[num] += 1
    print(mapp)
    
    j = 0
    for i in range(0,3):
        while i in mapp and mapp[i] > 0:
            nums[j] = i
            mapp[i] -= 1
            j += 1
    
sortColors()
print(nums)
