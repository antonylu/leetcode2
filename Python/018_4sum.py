"""
https://leetcode.com/problems/4sum/description/

Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

"""
xrange = range
import itertools
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # Approach #1, brute-force
        #
        # itertools.combination(), C(n,4)
        #
        # O(n!), 1%
        nums.sort()
        if sum(nums[:4]) > target: return []
        if sum(nums[-4:]) < target: return []
        ans = set()
        for c in itertools.combinations(nums,4):
            if sum(c) == target: ans.add(c)
        return sorted([list(c) for c in ans])


if __name__ == '__main__':
    s = Solution()
    tc =  [ ([1, 0, -1, 0, -2, 2],0), ([-3,-2,-1,0,0,1,2,3],0) ]
    ans = [ [ [-2, -1, 1, 2],  [-2,  0, 0, 2], [-1,  0, 0, 1] ], [[-3,-2,2,3],[-3,-1,1,3],[-3,0,0,3],[-3,0,1,2],[-2,-1,0,3],[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]] ]
    for i in range(len(tc)):
        r = s.fourSum(*tc[i])
        print (r)
        assert(r == ans[i])
