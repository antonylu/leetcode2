"""
https://leetcode.com/problems/shortest-unsorted-continuous-subarray/description/

Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.

"""
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Approach #1, brute-force
        #
        # sort first
        # compare sorted with unsorted
        #
        # find the index of first diff and last same
        # unsort = [2,5,4,8,10,9 ,15]
        # sorted = [2,4,5,8,9 ,10,15]
        # first ind = 1
        # last ind  = 5
        # ans = 5-1
        #
        # O(n log n) for sorted, 15%
        # 
        sortN = sorted(nums)
        n = len(nums)
        for i in range(n):
            if sortN[i]!=nums[i]: break

        if i == n-1: return 0
        j = n-1
        while sortN[j]==nums[j] and j >= 0:
            j-=1
        return j-i+1


if __name__ == '__main__':
    s = Solution()
    tc  = [ [2, 6, 4, 8, 10, 9, 15],[1,2,3,4,5],[5,4,3,2,1],[1] ]
    ans = [ 5,0,5,0 ]

    for i in range(len(tc)):
        r = s.findUnsortedSubarray(tc[i])
        print (r)
        assert(r == ans[i])
