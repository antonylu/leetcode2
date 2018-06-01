"""
https://leetcode.com/problems/max-consecutive-ones/description/


Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000

"""
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Approach #2, bytearray
        # O(n), 61ms, 100%
        #
        a = bytearray(nums).split(b'\x00')
        max = 0
        for i in a:
            max = max if max > len(i) else len(i)
        
        return max

        # Approach #1, naive
        # O(n), 2.35%
        #
        count = 0
        ans = 0
        for i in nums:
            if i == 1:
                count +=1
            else:
                ans = ans if ans > count else count
                count = 0

        return ans if ans > count else count
        


if __name__ == '__main__':
    s = Solution()
    tc = [[1,1,0,1,1,1]]
    an = [3]
    for i in range(len(tc)):
        print (s.findMaxConsecutiveOnes(tc[i]))
        #assert(s.findMaxConsecutiveOnes(tc[i][0],tc[i][1]) == an[i])
