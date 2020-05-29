"""
Problem:
  Start with an infinite two dimensional grid filled with zeroes, indexed from (1,1) at the bottom left corner with coordinates 
  increasing toward the top and right. Given a series of coordinates (r, c), where r is the ending row and c is the ending column, 
  add 1 to each element in the range from (1, 1) to (r, c) inclusive. Once all coordinates are processed, determine how many cells 
  contain the maximal value in the grid.

  Example:
    upRight = ["1 4", "2 3", "4 1"]

    The two space-separated integers within each string represent r and c respectively. The maximal value in the grid is 3, and there 
    is 1 occurrence at cell (1, 1).

  Function Description:
    Complete the function countMax in the editor below.

    countMax has the following parameter(s):
      string upRight[n]: an array of strings made of two space separated integers, r and c.

    Return:
      long: the number of occurrences of the final grid's maximal element.

    Constraints:
      1 <= n <= 100
      1 <= number of rows, number of columns <= 10^5



Solution:
"""

def countMax(upRight):
  r = []
  c = []
  for st in upRight:
    x,y = map(int, st.split(" "))
    r.append(x)
    c.append(y)
  
  return min(r) * min(c)

print(countMax(['1 4', '2 3', '4 1']))
print(countMax(['2 3', '3 7', '4 1']))