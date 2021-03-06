"""
https://leetcode.com/problems/integer-to-roman/description/

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII,
which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII.
Instead, the number four is written as IV. Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9.
    X can be placed before L (50) and C (100) to make 40 and 90.
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: 3
Output: "III"
Example 2:

Input: 4
Output: "IV"
Example 3:

Input: 9
Output: "IX"
Example 4:

Input: 58
Output: "LVIII"
Explanation: C = 100, L = 50, XXX = 30 and III = 3.
Example 5:

Input: 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

"""
xrange = range
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # Approach #1, straight forward
        # look-up table
        # 1~3999
        # breaks to 4 digits 3 9 9 9
        # 3 [0,1,2,3] => ["","M", "MM", "MMM"]
        # 9 [0,1,2,3,4,5,6,7,8,9] => ["","C", "CC", "CCC", "CD", "D", "DC","DCC","DCCC","CM"]
        # 9 [0,1,2,3,4,5,6,7,8,9] => ["","X", "XX", "XXX", "XL", "L", "LX","LXX","LXXX","XC"]
        # 9 [0,1,2,3,4,5,6,7,8,9] => ["","I", "II", "III", "IV", "V", "VI","VII","VIII","IX"]
        #
        # O(1), 68ms, 100% , way ahead of the 2nd 105ms
        #
        roman = [   ["","I", "II", "III", "IV", "V", "VI","VII","VIII","IX"],
                    ["","X", "XX", "XXX", "XL", "L", "LX","LXX","LXXX","XC"],
                    ["","C", "CC", "CCC", "CD", "D", "DC","DCC","DCCC","CM"],
                    ["","M", "MM", "MMM"]                                     ]
        ans = ""
        i  = 0
        while num >0:
            num, r = divmod(num,10)
            ans = roman[i][r] + ans
            i+=1
        return ans


if __name__ == '__main__':
    s = Solution()
    tc =  [ 3,4, 9,58,1994]
    ans = [ "III", "IV", "IX", "LVIII", "MCMXCIV"]
    for i in range(len(tc)):
        r = s.intToRoman(tc[i])
        print (r)
        assert(r == ans[i])
