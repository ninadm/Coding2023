'''
Description: Given a non-negative integer n, write a recursive function to calculate the sum of its digits.
Input: 12345
Output: 15 (because 1 + 2 + 3 + 4 + 5 = 15)
'''

def sum_of_digits(num): 
    while num > 9:
        ans = 0
        temp = num
        while temp:
            ans += (temp % 10)
            temp = temp // 10
        num = ans
    return num

print(sum_of_digits(10))
print(sum_of_digits(9))
print(sum_of_digits(11))
print(sum_of_digits(9998))