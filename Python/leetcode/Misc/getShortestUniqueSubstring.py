import pdb

def get_shortest_unique_substring(arr, string):
    '''
    xyyzyzyx
    arr = ['x', 'y', 'z']
    '''
    # pdb.set_trace()
    dictionary = {c: 0 for c in arr}
    startPointer = 0
    tailPointer = 0
    uniques = 0

    while tailPointer < len(string):
        if string[tailPointer] in dictionary:
            if dictionary[string[tailPointer]] == 0:
                uniques += 1
            dictionary[string[tailPointer]] += 1
            tailPointer += 1
            while uniques == len(arr):
                if len(string[startPointer:tailPointer]) == len(arr):  # condition where we have found a valid solution
                    return string[startPointer:tailPointer]
                else:
                    while startPointer < tailPointer and uniques == len(arr):
                        dictionary[string[startPointer]] -= 1
                        if dictionary[string[startPointer]] == 0:
                            uniques -= 1
                        startPointer += 1

    return string[startPointer:tailPointer]

print(get_shortest_unique_substring(['x', 'y', 'z'], "xyyzyzyx"))
