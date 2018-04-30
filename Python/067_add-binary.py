""" 
https://leetcode.com/problems/add-binary/description/

Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # convert string to binary
        # add
        # convert binary to string
        # 99%, 36ms
        v1 = int(a,base=2)
        v2 = int(b,base=2)
        sum = v1+v2
        s = bin(sum)
        return s[2:]
        

s = Solution()
test_case = [["11","1"], ["1010","1011"]]
for i in test_case:
    print(s.addBinary(i[0],i[1]))
