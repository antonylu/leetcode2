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
        """
        for i in range(len(nums)):
            if target <= nums[i]: return i 
        return i+1
        """
        # Solution 2: binary search, Divide and Conqure O(log n)
        # 99%, 33ms
        min = 0
        max = len(nums) - 1
        while (min <= max):
            mid = (min+max)//2
            if (nums[mid] == target):
                return mid
            if nums[mid] < target:
                min = mid+1
            else:
                max = mid-1
        return min

d = Solution()

a1 = ([1,3,5,6], 5)
a2 = ([1,3,5,6], 2)
a3 = ([1,3,5,6], 7)
a4 = ([1,3,5,6], 0)
a5 = ([1,3], 2)

print(d.searchInsert(a1[0],a1[1]))
print(d.searchInsert(a2[0],a2[1]))
print(d.searchInsert(a3[0],a3[1]))
print(d.searchInsert(a4[0],a4[1]))
print(d.searchInsert(a5[0],a5[1]))