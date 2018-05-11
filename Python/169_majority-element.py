"""
https://leetcode.com/problems/majority-element/description/
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
"""
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Approach #2, use list.count method
        #
        # Approach #3, sort list and return the middle element
        # in a sorted list, the majority number number are so many that the middle must be it
        # 43ms, 99%
        nums.sort()
        return nums[len(nums)//2]

        # Approach #1, brute force
        # enumerate every element, keep counter of each element with hash
        # if dict[element] > len(nums)/2: return element
        # O(n) 124ms, 4%
        dict = {}
        for i in nums:
            dict[i] = 1 if i not in dict else dict[i] + 1
            if dict[i] > len(nums)/2: return i
        

if __name__ == "__main__":
    s=Solution()
    tc = [[3,2,3],[2,2,1,1,1,2,2]]
    #tc = [1]
    for t in tc:
        print(s.majorityElement(t))
        #s.convertToTitle(t)
