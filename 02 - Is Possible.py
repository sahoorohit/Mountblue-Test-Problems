"""
Problem:
  Consider a pair of integers, (a, b). The following operations can be performed on (a, b) in any order, zero or more times:
    (a, b) -> (a + b, b)
    (a, b) -> (a, a + b)

  Return a string that denotes whether or not (a, b) can be converted to (c, d) by by performing zero or more of the operations specified above.

  Example: 
    (a, b) = (1, 2)
    (c, d) = (5, 2)

    Perform the operation (1, 1 + 1) to get (1, 2), 
    perform the operation (1 + 2, 2) to get (3, 2), and 
    perform the operation (3 + 2, 2) to get (5, 2). 
    
    Alternatively the first operation could be (1 + 1, 1) to get (2, 1) and so on. 

  Function Description:
    Complete the function isPossible in the editor below.

    isPossible has the following parameter(s):
      int a: first value in (a, b)
      int b: second value in (a, b)
      int c: first value in (c, d)
      int d: second value in (c, d)
    
    Returns:
      str: Return "Yes" if (a, b) can be converted to (c, d) by performing zero or more of the operations specified above, or "No" if not.

  Constraints:
    1 <= a, b, c, d <= 1000



Solution:
"""

def isPossible(a, b, c, d):
    
  if(c<a or d<b):
    return "No"
  if(a == 0 and b == 0):
    return "No"
  if(a == c and b == d):
    return "Yes"
  
  end = (c, d)
      
  x = [(a, a+b), [a+b, b]]
  loop = True
  res = False
  
  while(loop):
    y = []
    for i in range(len(x)):
        
      m = x[i]
      
      if(m == end):
        res = True
        loop = False
        break
      else:
        if(m[0] + m[1] <= end[1]):
          y.append((m[0], m[1]+m[0]))
    
        if(m[0] + m[1] <= end[0]):
          y.append((m[0]+m[1], m[1]))
                                                         
    if(len(y) == 0):
        loop = False
    x = y

  if(res):
    return "Yes"
  else:
    return "No"

print(isPossible(1, 1, 5, 2))
print(isPossible(1, 1, 2, 5))
print(isPossible(1, 4, 5, 10))
print(isPossible(1, 4, 1, 4))
print(isPossible(1, 0, 1, 1))