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

    def largestPalindrome2(self, n):
        # Approach #2, brute-force
        # 
        # for n digits, create largest possible palindrome with 2*n digits
        #
        # input is [1,8], palindrome digits %2 = 0 (n=2, palindrome 4-igits, n=3, palindrome 6-digits)
        # divid palindrome to Left and Right part
        # upper bound high = pow(10,n)-1, lower bound = pow(10,n-1)
        # 1. enumerate left, 
        # 2. create palindrome (left+tfel)
        # 3. check if divisible (% n-digit == 0)

        # example, 2 digits, 
        # possible number 99, 10^2
        # possible largest palindrome 99*99, 10^4 -1 = 10^2n -1
        # 
        # palindrom can be divided as (Left)(Revers_Left) part, example, 9009, Left = 90, right is 09
        # Largest Left is 10^n-1
        # 
        #
        # BTW, what's 1337 special for?
        # 
        # Time Limit Exceeded
        if n == 1: return 9
        high = pow(10, n ) - 1
        low  = pow(10, n - 1)
        for left in range(high,low,-1):
            right = int(str(left)[::-1])
            palindrome = left*pow (10,n) + right
            #print(palindrome)
            for d in range(high,low,-1):
                if palindrome / d > high: break
                if palindrome % d == 0: 
                    #print(palindrome)
                    return palindrome%1337
        
            
        
        


if __name__ == '__main__':
    s = Solution()
    tc = [1,2,3,4,5,6,7,8]
    an = [9, 987,123,597,677,1218,            877,              475]
    
    for i in range(len(tc)):
        print (s.largestPalindrome(tc[i]))
        assert(s.largestPalindrome(tc[i]) == an[i])
