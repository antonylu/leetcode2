"""
https://leetcode.com/problems/longest-continuous-increasing-subsequence/description/

Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).

Example 1:
Input: [1,3,5,4,7]
Output: 3

Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3.
Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4.

Example 2:
Input: [2,2,2,2,2]
Output: 1

Explanation: The longest continuous increasing subsequence is [2], its length is 1.
Note: Length of the array will not exceed 10,000.

"""
class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


        # Approach #1, naive
        #
        # compare 1 by 1
        # O(n), 17%
        #
        if len(nums) == 0 : return 0
        ans = 1
        count = 1
        current = nums[0]
        for i in range(1,len(nums)):
            if nums[i] > current:
                count +=1
            else:
                if count > ans: ans = count
                count = 1
            current = nums[i]
        if count > ans: ans = count
        return ans






if __name__ == '__main__':
    s = Solution()
    tc  = [ [1,3,5,4,7],[2,2,2,2,2],[],[1,3,5,7] ]
    ans = [ 3,1,0,4 ]

    for i in range(len(tc)):
        r = s.findLengthOfLCIS(tc[i])
        print (r)
        assert(r == ans[i])
