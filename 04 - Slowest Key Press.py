"""
Problem:
  A manufacturer is testing a new keyboard design. They are giving a typing test to a population and want to find out which key takes 
  the longest time to press. Given the result of a test, determine which key takes the longest to press.

  Example:
    keyTimes = [[0,2], [1,5], [0,9], [2,15]]

    Interpret each keyTimes[i][0] as an encoded character in the range ascii[a-z] where a = 0, b = 1, ..., z = 25. The second element, 
    keyTimes[i][1] represents the time the key is pressed since the start of the test. In this example, keys pressed, in order 
    are 0102(encoded) = abac at times 2, 5, 9, 15. From the start time it took 2 - 0 = 2 to press the first key, 5 - 2 = 3 to press 
    the second, and so on. The longest time it took to press a key was 2, or 'c', at 15 - 9 = 6. 

  Function Description:
    Complete the function slowestKey in the editor below. The function must return a character, the slowest key that Alex presses.

    slowestKey has the following parameter(s):
      int keyTimes[n][2]: the first column contains the encoded key pressed, the second contains the time at which it was pressed.

    Returns:
      character: the key that took the longest time to press

    Constraints: 
      1 <= n <= 10^5
      0 <= keyTimes[i][0] <= 25 (0 <= i < n)
      1 <= keyTimes[i][1] <= 10^8 (0 <= i < n)
      There will only be one key with the worst time.



Solution:
"""

def slowestKey(keyTimes):
  ch = keyTimes[0][0]
  slowestTime = keyTimes[0][1]

  for i in range(len(keyTimes)-1):
    currTime = keyTimes[i+1][1] - keyTimes[i][1]
    if(currTime > slowestTime):
      slowestTime = currTime
      ch = keyTimes[i+1][0]

  return chr(ch + 97)

print(slowestKey([[0,2], [1,5], [0,9], [2,15]]))