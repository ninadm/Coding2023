'''
Given a string s, find the length of the longest 
substring
 without repeating characters.


 Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

'''

def longestWithoutRepeating(s):
    count = 0
    res = set()
    for i in range(len(s)):
        if s[i] not in res:
            res.add(s[i])
            count = max(count, len(res))
        else:
            res = set(s[i])
    return count
print(longestWithoutRepeating('aabb'))


