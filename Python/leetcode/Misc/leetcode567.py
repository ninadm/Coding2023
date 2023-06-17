'''
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
let's come back to this, I think I can come up with a solution if I use a lot of space. 
that is what the hold up is. how to use less space!

'''

class Solution:
    def leetcode567(self, s1, s2):
        hashmap = {}
        for i in range(len(s1)):
            if s1[i] in hashmap:
                hashmap[s1[i]] += 1
            else:
                hashmap[s1[i]] = 1
        count = 0
        for i in range(len(s2)):
            while s2[i] in hash