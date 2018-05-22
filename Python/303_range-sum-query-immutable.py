"""
https://leetcode.com/problems/range-sum-query-immutable/description/


Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.
"""


# Approach #3, conversion
# convert nums into another array where sum[i+1] is the sum of nums[0:i+1], sum[0] = 0
# sumRange(i,j) = sum[j+1]-sum[i]
#
# nums[-2, 0, 3, -5, 2, -1] ==> sum[0,-2,-2,1,-4,-2,-3]
# sumRange(0, 2) = sum[2+1]-sum[0] = sum[3] - 0 = 1
# sumRange(2, 5) = sum[5+1]-sum[2] = (-3) - (-2) = -1
#
# sumRange(): O(1), 580ms, 24%
#
class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.sum = [0]
        for i in range(len(nums)):
            self.sum.append(sum(nums[0:i+1]))
        #print(self.sum)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sum[j+1] - self.sum[i]


# Approach #2, hash for cache
#
# keep the nums
# keep (i,j) in hash table for sum i to j 
#
# sumRange(): O(n)~O(1)
# 935ms, 11%, even slower?
class NumArray2(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.n = nums
        self.dict = {}

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if (i,j) in self.dict:
            return self.dict[(i,j)]
        else:
            self.dict[(i,j)] = sum(self.n[i:j+1])
            return self.dict[(i,j)]


# Approach #1, naive
#
# keep the nums
# sum i to j every time
#
# sumRange(): O(n), 917ms, 14%
#
class NumArray1(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.n = nums

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return sum(self.n[i:j+1]  )
        


# Your NumArray object will be instantiated and called as such:

if __name__ == "__main__":
    test= [-2, 0, 3, -5, 2, -1]
    tc  = [(0, 2),(2, 5),(0, 5)]
    ans = [1,-1,-3]
    obj = NumArray(test)
    for t in tc:
        print( obj.sumRange(t[0],t[1]))

        