""" 
https://leetcode.com/problems/maximum-subarray/description/

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

"""
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Solution 1: brute force, enumerate all sub array and calculate the value, return maximum value, O(n^2)
        # 
        # Solution 2: Dynamic programming
        # divide and conqure, the final optimization is determined by every optimized solution of each sub-question
        # > For each item in the array, find the largest sum of any subarray ended in that item
        # > and it's either the current item alone [c] or the previous+current item [..c]
        # > Save the result in-place, so we just need to save the maximum of the current item and its previous+current item
        # > return the maximum of the array
        # Time O(n), 87% 46ms
        r = nums[0]
        for i in range(1, len(nums)):
            j = nums[i] + nums[i-1]
            if j > nums[i]: nums[i] = j
            if r < nums[i]: r = nums[i]
        return r
        # Solution 3: accumulate sum, remember the max, re-accumate if sum < 0
        # O(n), 36% 54ms
        """
        sum = 0
        maximum = nums[0]
        for i in nums:
            sum += i
            if maximum < sum: maximum = sum
            if sum <0: sum = 0
            #print(maximum)
        
        return maximum
        """

s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
