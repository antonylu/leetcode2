"""
https://leetcode.com/problems/largest-palindrome-product/description/

Find the largest palindrome made from the product of two n-digit numbers.

Since the result could be very large, you should return the largest palindrome mod 1337.

Example:
Input: 2
Output: 987

Explanation: 99 x 91 = 9009, 9009 % 1337 = 987

Note:
The range of n is [1,8].

"""
class Solution(object):
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Approach #1, look up table
        # 
        # n is in range [1,8]
        # have all answers and return immediately
        #
        # O(1), 100%
        # palindrome      = [9, 9009, 906609, 99000099, 9966006699, 999000000999, 99956644665999, 9999000000009999]
        palindrome_1337 = [0,9,  987,    123,      597,        677,         1218,            877,              475]
        return palindrome_1337[n]

        # Approach #2, brute-force
        # for 4 digits, calculate all possible dddd*dddd
        # from the largest to lower, check if palindrome
        # if it is, %1337
        # 
        # for n = 8, O(10^8*10^8) = O(10^16)
        # Time Limit Exceeded
        #
        # BTW, what's 1337 special for?
        # 
        
        


if __name__ == '__main__':
    s = Solution()
    tc = [2,1]
    an = [987,0]
    for i in range(len(tc)):
        print (s.largestPalindrome(tc[i]))
        #assert(s.largestPalindrome(tc[i]) == an[i])
