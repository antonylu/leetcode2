"""
https://leetcode.com/problems/relative-ranks/description/

Given scores of N athletes, find their relative ranks and the people with the top three highest scores, who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

Example 1:
Input: [5, 4, 3, 2, 1]
Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]

Explanation: The first three athletes got the top three highest scores, so they got "Gold Medal", "Silver Medal" and "Bronze Medal". 
For the left two athletes, you just need to output their relative ranks according to their scores.
Note:
N is a positive integer and won't exceed 10,000.
All the scores of athletes are guaranteed to be unique.

"""
class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        # Approach #1, naive
        # get the sorted list
        # create the rank mapping table
        # create the answer with mapping table
        # O(n), 53%
        s = sorted(nums,reverse=True)
        size = len(s)
        d = {}
        ans = []

        d[s[0]] = "Gold Medal"
        if size > 1: d[s[1]] = "Silver Medal"
        if size > 2: d[s[2]] = "Bronze Medal"
        for i, e in enumerate(s[3:]):
            d[e] = str(i+4)
        for j in nums:
            ans.append(d[j])
        return ans
            


if __name__ == '__main__':
    s = Solution()
    tc = [[5, 4, 3, 2, 1],[1,2,3,4,5,6],[1]]
    an = [["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"],['6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal'],['Gold Medal']]
    for i in range(len(tc)):
        print (s.findRelativeRanks(tc[i]))
        assert(s.findRelativeRanks(tc[i])== an[i])
