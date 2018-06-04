"""
https://leetcode.com/problems/base-7/description/

Given an integer, return its base 7 string representation.

Example 1:
Input: 100
Output: "202"

Example 2:
Input: -7
Output: "-10"

Note: The input will be in range of [-1e7, 1e7].
"""
class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        # Approach #1, naive
        # 100 -> 14*7 mode 2, 14= 7* 2 mode 0
        #
        # O(1) 95%
        #
        if num == 0: return "0"
        ans = ""
        d = abs(num)
        while d > 0:
            d,m = divmod(d,7)
            ans = str(m) + ans
        if num <0: ans = "-"+ans
        return ans
            
        


if __name__ == '__main__':
    s = Solution()
    tc = [100,-7,0]
    an = ["202","-10","0"]
    for i in range(len(tc)):
        print (s.convertToBase7(tc[i]))
        assert(s.convertToBase7(tc[i])== an[i])
