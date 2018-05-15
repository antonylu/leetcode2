"""
https://leetcode.com/problems/house-robber/description/

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
"""

class Solution(object):
    def rob2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Approach #1, brute force
        # 
        
        # Approach #2, recursive
        """
        rob(x) = nums[0]                                   if x = 0
                 max(nums[0], nums[1])                     if x = 1
                 max( rob(k-2) + nums[k], rob(k-1) )       if x = k
        """
        # DP + recursive
        # O(n), 33ms, 66%
        dict = {}
        def robHouse(x):
            if x not in dict: 
                if x == 0: return nums[0]
                if x == 1: return max(nums[0],nums[1])
                dict[x]= max( robHouse(x-2) + nums[x], robHouse(x-1) )
            return dict[x]

        if not nums: return 0
        return robHouse(len(nums)-1)
        
    def rob(self, nums):
        #
        # Approach #3, iteration
        # 32ms, 78%
        last, now = 0, 0
        for i in nums: 
            (last, now) = (now, max(last + i, now))
        return now

if __name__ == "__main__":
    s=Solution()
    tc = [[1,2,3,1],[2,7,9,3,1],[],[183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]]
    ans = [4,12,3365]
    for t in tc:
        print(s.rob(t))
