"""
https://leetcode.com/problems/missing-number/description/

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
"""
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Approach #1, brute-force
        # convert to set
        # enumerate if n in set
        # O(n), 70%, 48ms
        s = set(nums)

        for i in range(0,len(nums)+1 ):
            if i not in s: 
                return i


if __name__ == "__main__":
    tc = [[3,0,1],[9,6,4,2,3,5,7,0,1],[1,2,3,4,5,6,8,0]]
    ans = [2, 8, 7 ]
    s = Solution()
    for t in tc:
        print(s.missingNumber(t) )
