"""
https://leetcode.com/problems/longest-harmonious-subsequence/description/

We define a harmonious array is an array where the difference between its maximum value and its minimum value is exactly 1.

Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.

Example 1:
Input: [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].
Note: The length of the input array will not exceed 20,000.

"""
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Approach #1, use collections.Counter()
        #
        # find continuous pair (i and i+1) and add these two counts
        # find the largest sum
        #
        # O(n), 13%
        from collections import Counter
        c = Counter(nums)
        ans = 0
        for k,v in c.items():
            if k+1 in c:
                ans = max(ans, v+c[k+1])
        return ans
        


if __name__ == '__main__':
    s = Solution()
    tc  = [ [1,3,2,2,5,2,3,7] ]
    ans = [ 5 ]

    for i in range(len(tc)):
        r = s.findLHS(tc[i])
        print (r)
        assert(r == ans[i])
