"""
https://leetcode.com/problems/number-of-segments-in-a-string/description/



Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.

Please note that the string does not contain any non-printable characters.

Example:

Input: "Hello, my name is John"
Output: 5
"""
class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Approach #1, str.split()
        # O(n), 100%
        return len(s.split())
        
if __name__ == '__main__':
    s = Solution()
    tc = ["Hello, my name is John", "This is a test", ""]
    ans = [5, 4, 0]
    for t in tc:
        print(s.countSegments(t))
