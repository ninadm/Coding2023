'''
Given a string containing only digits, you need to split the string into valid IP addresses. An IP address consists of four integers (each integer ranging from 0 to 255) separated by periods. The string must be split in such a way that each resulting combination forms a valid IP address.

Write a backtracking algorithm to solve this problem and return a list of all valid IP addresses that can be formed from the given string.

Function signature: def restore_ip_addresses(s: str) -> List[str]:

Input:

s: A string containing only digits, representing the input string.
Output:

Return a list of strings, where each string represents a valid IP address that can be formed from the given string.
Note:

The input string will have a length between 4 and 12 characters (inclusive).
Leading zeros in each integer are not allowed, except for the integer 0 itself.
The order of the IP addresses in the output does not matter.
'''
