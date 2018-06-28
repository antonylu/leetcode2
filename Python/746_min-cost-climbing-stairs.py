"""
https://leetcode.com/problems/min-cost-climbing-stairs/description/

On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.

Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6

Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
Note:
cost will have a length in the range [2, 1000].
Every cost[i] will be an integer in the range [0, 999].

"""
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # Approach #1, recursion with memorization, DP
        #
        # Say f[i] is the final cost to climb to the top from step i.
        #     f[i] = cost[i] + min(f[i+1], f[i+2])
        # f(n)  = cost[n]                         , if n >= len(cost) -2
        #       = cost[n] + min(f[n+1], f[n+2])   , if n
        #
        # O(n^2) if no memorization
        # O(n)   with hashmap lookup, 16%
        last2 = len(cost) - 2
        d = {}
        def finalCost(n):
            if n >= last2 :
                return cost[n]
            if n not in d:
                d[n] = cost[n] + min(finalCost(n+1), finalCost(n+2) )
            return d[n]

        return min(finalCost(0), finalCost(1))



if __name__ == '__main__':
    s = Solution()
    tc =  [ [10, 15, 20], [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]]
    ans = [  15, 6 ]

    for i in range(len(tc)):
        r = s.minCostClimbingStairs(tc[i])
        print (r)
        assert(r == ans[i])
