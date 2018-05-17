"""
https://leetcode.com/problems/contains-duplicate-ii/description/

Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:

Input: [1,2,3,1], k = 3
Output: true
Example 2:

Input: [1,0,1,1], k = 1
Output: true
Example 3:

Input: [1,2,1], k = 0
Output: false
"""
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # Approach #2, DP, use hash map to save (value,index)
        # for i in nums, check if every number nums[i] is in dict, if yes, check if i-index <=k
        # else, update dict[nums[i]] = i, so every index in hash table are the largest (nearest)
        # O(n), 20%
        # improve with length check, 99%
        if not nums or k<0 or len(nums)==len(set(nums)):return False 
        dict = {}
        for i,v in enumerate(nums):
            if v in dict:
                if i - dict[v] <=k: return True
            dict[v] = i
        return False

        # Approach #1, brute-force
        # check every number nums[i] for any duplicate within range k nums[i+k]
        # O(n*k)
        # Time Limit Exceeded
        if k == 0: return False
        for i in range(len(nums)-1):
            curr = nums[i]
            j = i+1
            while j<len(nums) and j<=i+k:
                if nums[j] == curr: 
                    #print(i,j,curr)
                    return True
                j +=1
        return False
        

if __name__ == "__main__":
    s = Solution()
    tc  = [[1,2,1],[1,2,3,1],[1,0,1,1],[1,2,1],[1,2,3,4],[1,1,1,3,3,4,3,2,4,2],]
    kc  = [1,3,1,0,1,2]
    ans = [False,True,True,False,False,True,False]
    for t,k,a in zip(tc,kc,ans):
        print(s.containsNearbyDuplicate(t,k))
        assert(s.containsNearbyDuplicate(t,k) == a)
