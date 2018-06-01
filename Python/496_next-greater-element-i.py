"""
https://leetcode.com/problems/next-greater-element-i/description/


You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.

Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
Explanation:
    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.

Example 2:
Input: nums1 = [2,4], nums2 = [1,2,3,4].
Output: [3,-1]
Explanation:
    For number 2 in the first array, the next greater number for it in the second array is 3.
    For number 4 in the first array, there is no next greater number for it in the second array, so output -1.
Note:
All elements in nums1 and nums2 are unique.
The length of both nums1 and nums2 would not exceed 1000.
"""
class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        # Approach #2, dict
        # 
        # it is just a mapping table
        # the next greater number is 1 on 1 mapping,
        # so we can use dict to remember it, and look it up
        #
        # O(n) 68.25%
        dict ={}
        s_nums = len(nums)
        k = 0
        for j in range(s_nums):
            k = j+1
            dict[nums[j]] = -1
            while k < s_nums:
                if nums[k] > nums[j]:
                    dict[nums[j]] = nums[k]
                    break
                k +=1

        return [ dict[i] for i in findNums ]



if __name__ == '__main__':
    s = Solution()
    tc = [([4,1,2],[1,3,4,2]),([2,4],[1,2,3,4])]
    an = [[-1,3,-1],[3,-1]]
    for i in range(len(tc)):
        print (s.nextGreaterElement(tc[i][0],tc[i][1]))
        assert(s.nextGreaterElement(tc[i][0],tc[i][1]) == an[i])
