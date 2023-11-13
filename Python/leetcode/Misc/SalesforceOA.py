'''
Given two numbers A and B
Find all magical numbers. A magical number is a number if you can split the digits into 2 sets such that their sum is equal
'''

def magicalNumbers(a, b):
    
    def convertNumToArray(n):
        arr = []
        n = int(n)
        while n != 0:
            arr.append(n % 10)
            n = n // 10
        return arr

    def isMagicalNumber(arr):
        
        if sum(arr) % 2 != 0:
            return False
        
        def combinationSum(potentialSol, target, idx):
            if sum(potentialSol) == target:
                return True
            if idx == len(arr) or sum(potentialSol) > target:
                return False
            
            return combinationSum(potentialSol[:] + [arr[idx]], target, idx + 1) or combinationSum(potentialSol[:], target, idx + 1)

        status = combinationSum([], sum(arr) // 2, 0)
        if status:
            print(sum(arr), sum(arr)//2)
        return status
            

    if a < 10 and b < 10:
        return []
    if a < 10:
        a = 10
    ans = []
    for n in range(a, b + 1, 1):
        arr = convertNumToArray(n)
        if isMagicalNumber(arr):
            ans.append(n)
    return ans

print(magicalNumbers(37900, 37966))

