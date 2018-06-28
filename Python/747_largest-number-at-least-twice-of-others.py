"""
https://leetcode.com/problems/largest-number-at-least-twice-of-others/description/

In a given integer array nums, there is always exactly one largest element.

Find whether the largest element in the array is at least twice as much as every other number in the array.

If it is, return the index of the largest element, otherwise return -1.

Example 1:

Input: nums = [3, 6, 1, 0]
Output: 1
Explanation: 6 is the largest integer, and for every other number in the array x,
6 is more than twice as big as x.  The index of value 6 is 1, so we return 1.


Example 2:

Input: nums = [1, 2, 3, 4]
Output: -1
Explanation: 4 isn't at least as big as twice the value of 3, so we return -1.


Note:

nums will have a length in the range [1, 50].
Every nums[i] will be an integer in the range [0, 99].

"""
class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Approach #1, brute-force
        # sort and get 1st and 2nd largest element
        # if 1st >=2nd*2, binary search 1st
        #
        # O(n log n) for sorting, 32%
        if len(nums) == 1 : return 0
        num = sorted(nums, reverse = True)
        if num[0] < num[1]*2:
            return -1
        else:
            #print(num[0],nums)
            return nums.index(num[0])

        # Approach #2, linear search
        # linear search 1st and 2nd largest element
        # return 1st >=2nd*2
        #
        # O(n log n) for sorting









if __name__ == '__main__':
    s = Solution()
    tc =  [ [3, 6, 1, 0], [1, 2, 3, 4],[1]]
    ans = [  1, -1 ]

    for i in range(len(tc)):
        r = s.dominantIndex(tc[i])
        print (r)
        assert(r == ans[i])
