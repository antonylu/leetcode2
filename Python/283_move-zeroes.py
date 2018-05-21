"""
https://leetcode.com/problems/move-zeroes/description/


Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.

"""
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # Approach #1, brute-force, naive
        #
        # O(n^2), 60ms, 86%
        
        i = 0
        for c in range(len(nums)):
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
            else:
                i+=1
        
        
        
        

if __name__ == "__main__":
    tc = [[0,0,1],[0,1,0,3,12]]
    #tc = [2126753390]
    s = Solution()
    for t in tc:
        s.moveZeroes(t)
        print(t)
