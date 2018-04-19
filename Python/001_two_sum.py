# https://leetcode.com/problems/two-sum/
#
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# 
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# 
# Example:
# 
# Given nums = [2, 7, 11, 15], target = 9,
# 
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ## no1. brute force, enumeration, two nested loops
        ## space O(1)
        ## time  O(n^2), beats 4%, 6637ms
        #  
        #for i in range(0, len(nums)-1) :
        #    for j in range(i+1, len(nums)):
        #        if (target == nums[i]+nums[j] ):
        #            return [i,j]

                    
        # no2. memorization, hash table, put (target - nums[i]) in dict
        # if it exists then both found. One-pass hash table
        # hash table look up average = O(1)
        # space O(n)
        # time  O(n), beats 40%, 662 ms
        d = {}
        for i in range(0, len(nums)):
            if (nums[i] in d.keys() ): 
                return [d[nums[i]],i]
            else:
                d[(target- nums[i])] = i
