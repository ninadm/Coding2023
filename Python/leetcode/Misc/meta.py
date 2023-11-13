'''

You are given two lists of intervals, A and B.

In A, the intervals are sorted by their starting points. None of the intervals within A overlap.

Likewise, in B, the intervals are sorted by their starting points. None of the intervals within B overlap.

Return the intervals that overlap between the two lists.

Example:

A: {[0,4], [7,12]}
B: {[1,3], [5,8], [9,11]}
Return:

{[1,3], [7,8], [9,11]}

How would you do this?
'''
A = [[0,2], [5,9], [13,15]]
B = [[5,8], [9,14]]
def unionIntervals(A, B):
    answer = []
    i = 0
    j = 0

    while i < len(A) and j < len(B):
        # if there is overlap between i and j, we take that interval and move on from both i and j
        intervalA = A[i]
        intervalB = B[j]
        if intervalB[0] <= intervalA[0] <= intervalB[1] or intervalA[0] <= intervalB[0] <= intervalA[1]:
            answer.append([min(intervalA[0], intervalB[0]), max(intervalA[1], intervalB[1])])
            i += 1
            j += 1
        # 
        elif intervalA[0] < intervalB[0]:
            answer.append(intervalA)
            i += 1
        else:
            answer.append(intervalB)
            j += 1
    return answer

print(unionIntervals(A,B))
        



    

