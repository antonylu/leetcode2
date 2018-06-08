"""
https://leetcode.com/problems/k-diff-pairs-in-an-array/description/

Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. 
Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute difference is k.

Example 1:
Input: [3, 1, 4, 1, 5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.

Example 2:
Input:[1, 2, 3, 4, 5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).

Example 3:
Input: [1, 3, 1, 5, 4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).

Note:
The pairs (i, j) and (j, i) count as the same pair.
The length of the array won't exceed 10,000.
All the integers in the given input belong to the range: [-1e7, 1e7].
"""
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Approach #1,
        # 
        # if k < 0 : return 0
        # if k == 0: count how many integer appears more than twice, with collections.Counter()
        # if k > 0 : use set(nums) to remove duplicates.
        # for each element, check if e+k exists in the set
        #
        # O(n) + O(n)
        # 99.53%
        ans = 0
        if k == 0:
            from collections import Counter
            d = dict(Counter(nums))
            for k,v in d.items():
                if v > 1: ans +=1
            return ans
        if k < 0: return 0
        s = set(nums)
        for e in s:
            if e+k in s: ans+=1
        return ans


if __name__ == '__main__':
    s = Solution()
    tc  = [([3, 1, 4, 1, 5], 2),([1, 2, 3, 4, 5],1),([1, 3, 1, 5, 4],0), ([1,2,3,4,5],-1)]
    ans = [2,4,1,0]

    for i in range(len(tc)):
        r = s.findPairs(tc[i][0],tc[i][1])
        print (r)
        assert(r == ans[i])
