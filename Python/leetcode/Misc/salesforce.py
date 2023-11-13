'''

This question was asked in salesforce OA round for intern.
Bert has a fascination for sequences, he found a very nice problem with natural number sequences.
He has a number n, which indirectly implies that he has an integer sequence of [1, 2, 3, ..., n - 1]. 
Now he asks Ernie to remove the minimum amount of elements from this sequence, such that the 
product of all integers in the resulting sequence becomes congruent to 1 mod n. 
[i.e., if product of the resultant sequence is p, then p % n is 1]
NOTE:For all practical purposes, consider the product of an empty sequence to be 1.
If there are multiple solutions, return the lexicographically smallest one.
Return the array in increasing order only.
'''

def magicalSequence(n):
    