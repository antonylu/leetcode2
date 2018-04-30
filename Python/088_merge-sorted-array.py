""" 
https://leetcode.com/problems/merge-sorted-array/description/

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
"""
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # straightforward
        # 89% 40ms
        for i in range(n):
            nums1[m+i] = nums2[i]
        nums1.sort()
            
s = Solution()
#test_case = [[1,2,3,0,0,0],[2,5,6]]
i = [[1,2,3,0,0,0],[2,5,6]]
#for in in test_case:

s.merge(i[0],3,i[1],3)
print(i[0])

