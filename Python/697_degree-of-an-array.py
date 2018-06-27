"""
https://leetcode.com/problems/degree-of-an-array/description/

Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2

Explanation:
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.

Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6
Note:

nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.

"""
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Approach #1, count and subtract
        #
        # find degree with count.most()
        # answer = index of last - first + 1
        # O(n), 10%
        def rindex(mylist, myvalue):
            return len(mylist) - mylist[::-1].index(myvalue) - 1

        from collections import Counter
        c = Counter(nums).most_common()
        degree = c[0][1]
        ans = len(nums)
        for i in c:
            if i[1] != degree: break
            first = nums.index(i[0])
            last  = rindex(nums,i[0])
            ans = min(ans, last-first+1)
        return ans



if __name__ == '__main__':
    s = Solution()
    tc = [[1, 2, 2, 3, 1],[1,2,2,3,1,4,2]]


    ans = [ 2,6 ]


    for i in range(len(tc)):
        r = s.findShortestSubArray(tc[i])
        print (r)
        assert(r == ans[i])
