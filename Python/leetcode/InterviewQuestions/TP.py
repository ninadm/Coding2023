'''
This solution is wrong, it needs to be converted into a graph. Cannot solve with the intervals approach
'''
def areCirclesConnected(input_circles):
  x_axis = []
  y_axis = []
  
  for i in range(len(input_circles)):
    x_axis.append([input_circles[i][0] - input_circles[i][2], input_circles[i][0] + input_circles[i][2]])
    y_axis.append([input_circles[i][1] - input_circles[i][2], input_circles[i][1] + input_circles[i][2]])
  
  
  def areIntervalsConnected(intervals):
    intervals.sort(key=lambda x:x[0])
    for i in range(len(intervals) - 1):
      if intervals[i+1][0] > intervals[i][1]:
        return False
    return True
  
  
  return areIntervalsConnected(x_axis) and areIntervalsConnected(y_axis)

input_c = [[0, 0, 4], [0, 0, 3], [0, 0, 2]]

print(areCirclesConnected(input_c))