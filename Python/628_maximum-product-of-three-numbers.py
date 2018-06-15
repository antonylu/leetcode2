"""
https://leetcode.com/problems/maximum-product-of-three-numbers/description/

Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:
Input: [1,2,3]
Output: 6
Example 2:
Input: [1,2,3,4]
Output: 24

Note:
The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.

"""
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Approach #1, find the largest and check
        #
        # sort
        # [-1000, -900, -800, ... 800, 900, 1000]
        # the maximum maybe: 
        #  800*900*100
        #  -1000*-900*1000
        #  
        #  O(n log n) for sort, 6%
        nums.sort()
        return max(nums[-1]*nums[-2]*nums[-3], nums[-1]*nums[0]*nums[1])
        


if __name__ == '__main__':
    s = Solution()
    tc  = [ [1,2,3], [1,2,3,4],[-1000, -900, -800, 0,1, 800, 900, 1000]]
    ans = [ 6,24, 900000000 ]
    for i in range(len(tc)):
        r = s.maximumProduct(tc[i])
        print (r)
        assert(r == ans[i])
