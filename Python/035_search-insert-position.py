""" 
https://leetcode.com/problems/search-insert-position/description/

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0
"""
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        

        # search in a sorted array
        # Solution 1: brute force, enumerative, O(n)
        # 36%, 39ms
        for i in range(len(nums)):
            if target <= nums[i]: return i 
        return i+1
        # Solution 2: binary search, O(log n)


d = Solution()

haystack = 'hello'
needle = 'll'
print(d.strStr(haystack,needle))

haystack = "aaaaa"
needle = "bba"
print(d.strStr(haystack,needle))
