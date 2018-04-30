""" 
https://leetcode.com/problems/plus-one/description/

Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # plus 1 from right most digit, mode 10 and save carry
        # O(n), 85%, 36ms
        carry = 1
        for i in range(len(digits)-1,-1,-1):
            if carry == 1:
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i]+=1
                    carry = 0
                    return digits
        if carry == 1:
            r = [1]
            r.extend(digits)
            return r
        return digits

s = Solution()
test_case = [[1,2,3], [4,3,2,1],[9,9,9]]
for i in test_case:
    print(s.plusOne(i))
