"""
https://leetcode.com/problems/student-attendance-record-i/description/

You are given a string representing an attendance record for a student. The record only contains the following three characters:
'A' : Absent.
'L' : Late.
'P' : Present.
A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

You need to return whether the student could be rewarded according to his attendance record.

Example 1:
Input: "PPALLP"
Output: True

Example 2:
Input: "PPALLL"
Output: False
"""
class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Naive
        # O(n), 66.37%
        # return s.find("LLL")==-1 and s.count('A') < 2
        # O(n), 66.37%
        # return "LLL" not in s and s.count('A') < 2
        # O(n), 88%
        return s.count('A') < 2 and "LLL" not in s

if __name__ == '__main__':
    s = Solution()
    tc  = ["PPALLP", "PPALLL","AAAA"]
    ans = [True, False, False]

    for i in range(len(tc)):
        r = s.checkRecord(tc[i])
        print (r)
        assert(r == ans[i])
