"""
https://leetcode.com/problems/intersection-of-two-arrays/description/

Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:
Each element in the result must be unique.
The result can be in any order.
"""
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Approach #1, use set operation
        # 90%
        return list(set(nums1) & set(nums2))

if __name__ == '__main__':
    tc = [([1, 2, 2, 1,3,],[2, 2,3])]
    s = Solution()
    for t in tc:
        print(s.intersection(t[0],t[1]))


