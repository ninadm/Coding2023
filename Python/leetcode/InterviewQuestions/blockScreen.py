'''
Given a list of arrays with movie votes 
return the winning movie
input = list of list
[
['A','B','C']
['A', 'D', 'E']
]
Solve later
'''

def calculateScore(input):
    movieScoreName = (-1, '')
    for i in range(len(input)):
        for j in range(min(len(input[i]), 3)):
            currScore = 3 - (j%3)
            if movieScoreName[0] < movieScoreName[0] + currScore:
                movieScoreName = (movieScoreName[0] + currScore, input[i][j])
