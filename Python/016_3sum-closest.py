"""
https://leetcode.com/problems/3sum-closest/description/

Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target.
Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

"""
xrange = range
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Approach #1, brute-force
        # enumerate all possible 3 integers
        # O(n^k)
        #

        # Approach #2, brute-force, linear search
        #
        # sort first
        # for every i in nums:
        #    j, k from min,max
        #    keep enumerate to the middle and track closest to target, or return match target
        #    move j, k depends on sum(i,j,k) > target?
        #
        # O(n^2), 98%
        #
        nums.sort()
        ans = sum(nums[:3])
        if ans == target: return target
        for i in xrange(len(nums[:-2])):
            j = i+1
            k = len(nums)-1
            while j<k:
                s = nums[i]+nums[j]+nums[k]
                if s == target: return target
                if abs(target-s) < abs(target - ans): ans = s
                if s > target:
                    k-=1
                else:
                    j+=1

        return ans



if __name__ == '__main__':
    s = Solution()
    tc =  [ ([-1, 2, 1, -4],1)]
    ans = [ 2 ]
    for i in range(len(tc)):
        r = s.threeSumClosest(*tc[i])
        print (r)
        assert(r == ans[i])
