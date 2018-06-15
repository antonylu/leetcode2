"""
https://leetcode.com/problems/maximum-average-subarray-i/description/

Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

Example 1:
Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75


Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75

Note:
1 <= k <= n <= 30,000.
Elements of the given array will be in the range [-10,000, 10,000].


"""
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # Approach #1, sliding window
        # O(n), 98%
        window = sum(nums[:k])
        ans = window
        for i in range(k,len(nums)):
            window = window + nums[i] - nums[i-k]
            if ans < window: ans = window
        return ans/float(k)
        


if __name__ == '__main__':
    s = Solution()
    tc  = [ ([1,12,-5,-6,50,3], 4)]
    ans = [ 12.75]
    for i in range(len(tc)):
        r = s.findMaxAverage(tc[i][0],tc[i][1])
        print (r)
        assert(r == ans[i])
