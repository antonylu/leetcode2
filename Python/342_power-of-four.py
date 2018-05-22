"""
https://leetcode.com/problems/power-of-four/description/


Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example:
Given num = 16, return true. Given num = 5, return false.

Follow up: Could you solve it without loops/recursion?

"""
class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """


        # Approach #1, naive
        #
        # power of 3 are 1,3,9,27,81...
        # continue divide it by 3 would result 1
        #
        # O(n), 64%
        if num == 0: return False
        if num == 1: return True
        while num%4 == 0:
            num=num/4

        return num == 1
        

        


# Your NumArray object will be instantiated and called as such:

if __name__ == "__main__":
    tc  = [16,5,0,4,1,-3,2,8]
    ans = [True, False,False,True,True,False,False,False]
    s = Solution()
    for i in range(len(tc)):
        print( s.isPowerOfFour(tc[i]))
        assert(s.isPowerOfFour(tc[i]) == ans[i])