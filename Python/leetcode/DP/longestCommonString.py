'''
axyb
abyxb
axb

aa
xayaz
aa

a
z
None

abracadabra
avadakedavra
aaadara


_ _ _ _ _ _ _ _ _ _ _ _
0 None 10 2 None 4 3 8 10 11 



aaadara

Tabulation
Recursion


'''

def longest_lcs(A, B):
    memo = {}

    def rec(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        if i == 0 or j == 0:
            result = ""
        elif A[i - 1] == B[j - 1]:
            result = rec(i - 1, j - 1) + A[i - 1]
        else:
            lcs1 = rec(i - 1, j)
            lcs2 = rec(i, j - 1)
            if len(lcs1) > len(lcs2):
                result = lcs1
            else:
                result = lcs2
        memo[(i, j)] = result
        return result

    return rec(len(A), len(B))


print(longest_lcs("abracadabra", "avadakedavra"))

