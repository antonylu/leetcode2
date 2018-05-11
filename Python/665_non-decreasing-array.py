"""
https://leetcode.com/problems/non-decreasing-array/description/

Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

Example 1:
Input: [4,2,3]
Output: True
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.

Example 2:
Input: [4,2,1]
Output: False

Explanation: You can't get a non-decreasing array by modify at most one element.
Note: The n belongs to [1, 10,000].
"""

class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Approach #1, brute force, check every two elements 
        # assert array[i] <= array[i + 1]
        # if assert twice, return False
        # else return True
        # O(n)

        # if nums[i] > nums[i + 1] occurs, we need to make sure 
        #  nums[i] can be modified to value of nums[i+1] (decreasing) and still meet nums[i-1] < nums[i],  i.e., nums[i-1] <= nums[i+1]
        #   or
        #  nums[i+1] can be modified to value of nums[i] (increasing) and still meet nums[i+1] < nums[i+2],i.e., nums[i] <= nums[i+2]
        # for example, case [3,4,2,3]
        #  [ 3 ,4,  2,  3]
        #  [i-1,i,i+1,i+2]
        # b[ 3 ,2,  2,  3] nums[i-1] <= nums[i+1] 
        # a[ 3 ,4,  4,  3]   nums[i] <= nums[i+2] 
        # 
        # 57ms, 96%
        c = 0
        l = len(nums)
        for i in range(l -1):
            if nums[i]>nums[i+1]: 
                c +=1
                if c > 1 or ((i>0 and nums[i-1] > nums[i+1]) and (i+2<l and nums[i] > nums[i+2] )):
                    return False
        return True
        

if __name__ == "__main__":
    s=Solution()
    tc = [[4,2,3],[4,2,1],[3,4,2,3]]
    for t in tc:
        print(s.checkPossibility(t))
