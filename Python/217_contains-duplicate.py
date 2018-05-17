"""
https://leetcode.com/problems/contains-duplicate/description/

Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true

"""
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Approach #1, brute-force
        # iteration, comparing every number with the rest numbers
        # n-1 + n-2 + ... + 1 = n*(n-1)/2
        # O(n^2)
        
        # Approach #2, use Set
        # if no duplicates, len(set(nums)) == len(nums)
        # O(n), 52ms, 53%
        return len(set(nums)) != len(nums)


if __name__ == "__main__":
    s = Solution()
    tc  = [[1,2,3,1],[1,2,3,4],[1,1,1,3,3,4,3,2,4,2]]
    ans = [True,False,True]
    for t in tc:
        print(s.containsDuplicate(t))
