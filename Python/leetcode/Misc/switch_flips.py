'''
11011

'''
def minSwitchFlips(seq):

    def backtrack(pos, inp, flips):
        if pos == len(seq):
            return flips
        if inp[pos] == '0' and pos - 1 >= 0 and inp[pos - 1] == '1': 
            first = backtrack(pos + 1, inp[:pos - 1] + ['0'] + inp[pos:], 1 + flips)
            second = backtrack(pos + 1, inp[:pos] + ['1'] + inp[pos+1:], 1 + flips)
            return min(first, second)
        return backtrack(pos + 1, inp[:], flips)
    
    return backtrack(1, list(seq), 0)

print(minSwitchFlips('01010'))

