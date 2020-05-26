"""
Problem:
  A video game developer has designed a video game in which the character can be programmed to move around the screen in 4 different directions: 
  Up (U), Down (D), Left (L), and Right (R). The character movement needs to be optimized by deleting unnecessary directions while maintaining 
  the same destination. Given the original set of directions, what is the maximum number of instructions that can be deleted and still have 
  the character reach the destination?

  Note: The instructions that are deleted do not need to be contiguous.

  Example:
    s = 'URDR'

    Given an original set of instructions s = 'URDR', the final destination is 2 units to the right of the initial position after the 
    character moves up, right, down, and right. If 'U' and 'D' are deleted, the destination remains the same. The answer 2 will be returned.

  Function Description:
    Complete the function getMaxDeletions in the editor below.

    getMaxDeletions has the following parameter:
      string s: the original instructions that were programmed

    Returns: 
      int: the maximum number of instructions that can be deleted from s while maintaining the destination.

  Constraints:
    1 <= n <= 10^5
    s contains only the characters 'U', 'D', 'L', and 'R'



Solution:
"""

def getMaxDeletions(s):
  n = len(s)
  u = s.count('U')
  d = s.count('D')
  r = s.count('R')
  l = s.count('L')
  
  return n - (abs(u-d) + abs(r-l))
    
print(getMaxDeletions('URDR'))
print(getMaxDeletions('RUDRL'))
print(getMaxDeletions('RRR'))
print(getMaxDeletions('RURUR'))