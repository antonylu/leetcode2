"""
https://leetcode.com/problems/sum-of-two-integers/description/

Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.


"""
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # Approach #1, bit manipulation
        #
        # to add 1 bit number
        #  xor ^ to get result,    0^0, 1^1 -> 0, 0^1, 1^0 -> 1
        #  and & to get carry bit, 1&1 -> 1, others 0
        # extend this method to 32 bits
        #
        # a^b add all no  carry bits
        # a&b get all the carry bits, (a&b) <<1 get the carried result
        # continue add them into a until carry is 0
        # 
        # This only works with Positive Integers
        while ( b != 0):
            carry = a & b
            a = a ^ b
            b = (carry << 1)
        return a
                    
                

if __name__ == '__main__':
    tc = [(-1,1),(16,14),(15,4),(2,1),(0,5)]
    s = Solution()
    for i in range(len(tc)):
        print(s.getSum(tc[i][0],tc[i][1]))
        assert(s.getSum(tc[i][0],tc[i][1]) == tc[i][0] + tc[i][1])

