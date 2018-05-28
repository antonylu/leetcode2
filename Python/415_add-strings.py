"""
https://leetcode.com/problems/add-strings/description/


Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # Approach #2, naive
        # convert string to integer
        # convert integer to string
        # O(n) 55%
        def str2int(s):
            str2int = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9 }
            n = 0
            for c in s:
                n = n*10 + str2int[c]
            return n
        return str(str2int(num1)+str2int(num2))

    def addStrings1(self, num1, num2):
        # Approach #1, naive
        # convert string to integer
        # convert integer to string
        # 99%, cheating
        return str(int(num1)+int(num2))
            
        
if __name__ == '__main__':
    s = Solution()
    tc = [("3","6"), ("12312","213123")]
    ans = ["9","225435"]
    for t in tc:
        print(s.addStrings(t[0],t[1]))
