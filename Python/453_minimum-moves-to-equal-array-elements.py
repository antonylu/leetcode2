"""
https://leetcode.com/problems/minimum-moves-to-equal-array-elements/description/

Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements equal, where a move is incrementing n - 1 elements by 1.

Example:
Input:
[1,2,3]
Output:
3

Explanation:
Only three moves are needed (remember each move increments two elements):

[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
"""
class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Approach #1, math
        #
        # m: moves, 
        # n: number of elements
        # x: final number
        # min: minimum umber
        #
        #   sum + m * (n - 1) = x * n
        #   x = min + m, because min always need add value to reach x
        #   sum + m*n - m = (min+m)*n = min*n + m*n
        #   m = sum - min*n
        #  
        #  O(n), 77%
        return sum(nums) - min(nums)*len(nums)
        
        

if __name__ == '__main__':
    s = Solution()
    tc = [[1,2,3],[4,3,2,7,8,2,3,1]]
    an = [3,22]
    for i in range(len(tc)):
        print(s.minMoves(tc[i]))
        assert(s.minMoves(tc[i]) == an[i])
