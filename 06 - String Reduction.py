"""
Problem:
  Given a string, reduce it in such a way that all of its substrings are distinct. To do so, you may delete any character at any index. 
  What is the minimum number of deletions needed?

  Note: A substring is a contiguous group of 1 or more character within a string.

  Example:
    s = "abab"

    Substrings in s are {'a', 'b', 'a', 'b', 'ab', 'ba', 'ab', 'aba', 'bab', 'abab'}. By deleting one "a" and one "b", the string becomes 
    "ab" or "ba" and all of its substrings are distinct. This required 2 deletions.

  Function Description:
    Complete the function getMinDeletions in the editor below.

    getMinDeletions has the following parameter(s):
      string s: the given string 
    Returns:
      int: the minimum number of deletions required

  Constraints:
    1 <= n <= 10^5



Solution:
"""

def getMinDeletions(s):
  return len(s) - len(set(s))
    
    
print(getMinDeletions("abab"))
print(getMinDeletions("abcab"))
print(getMinDeletions("abcabc"))
