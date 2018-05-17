"""
https://leetcode.com/problems/power-of-two/description/

Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true
Example 2:

Input: 16
Output: true
Example 3:

Input: 218
Output: false
"""
power2=set([1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824, 2147483648, 4294967296, 8589934592])
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Approach #2, bitwise operation
        # if n is power of 2, the binary form has only one bit in 1, the other bits are all 0
        # example,          n-1:
        #  1: 00000001    0: 00000000
        #  2: 00000010    1: 00000001
        #  4: 00000100    3: 00000011
        #  8: 00001000    7: 00000111
        #  
        # n&(n-1)=0
        # O(1),  44ms, 72%
        if n ==0: return False
        return n&(n-1)==0

        # Approach #1, lookup table
        # O(1)
        # 43ms, 81%
        return n in power2
        

        



if __name__ == "__main__":
    tc = [0,1,16,218]
    a  = [True,True,False]
    s = Solution()
    for test in tc:
        print(s.isPowerOfTwo(test))
        #assert(s.isPowerOfTwo(test) == )
