"""
Problem:
  We define an array of integers in meandering order to be an array where the first two elements are the respective largest and smallest 
  elements in the array and the subsequent element alternate between its next largest and next smallest elements. In other words, the 
  elements are in order or [first_largest, first_smallest, second_largest, second_smallest, ...]. 

  For example, the array [-1, 1, 2, 3, -5] sorted normally is [-5, -1, 1, 2, 3]. Sorted in meandering order, it becomes [3, -5, 2, -1, 1].

  Function Description:
    Complete the function meanderingArray in the editor below. The function must return an array of integers sorted in meandering order.

    meanderingArray has the following parameter(s):
      unsorted[unsorted[0],...unsorted[n-1]]: an array of integers

  Constraints 
    2 <= n <= 10^4
    -10^6 <= unsorted[i] <= 10^6
    The sorted array may contain duplicate elements.



Solution:
"""

def meanderingArray(unsorted):
  unsorted.sort()

  res = []
  smInd = 0
  laInd = len(unsorted) - 1

  for i in range(len(unsorted)):
    if(i%2 == 0):
      res.append(unsorted[laInd])
      laInd -= 1
    else:
      res.append(unsorted[smInd])
      smInd += 1

  return res

print(meanderingArray([-1, 1, 2, 3, -5]))
