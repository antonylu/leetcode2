""" 
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Approach #1, 
        # find a bottom as buy point
        # whenever a lower price, bottom is updated
        # whenever a higher price, 
        #   cash out as if we bought it at bottome and sell it at the high price
        #       sum += (todays' price -bottom)
        #   set the bottom as today's price
        #
        # O(n), 15.23%, 55ms
        # improve by removing list dereference
        # O(n), 99%, 37ms
        # Python 3: 100% 40ms
        if not prices: return 0
        sum = 0
        bottom = prices[0]
        for i in prices:
            if i > bottom:
                sum += (i - bottom)
            bottom = i
        return sum


        
        


if __name__ == "__main__":
    tc  = [[7,1,5,3,6,4],[1,2,3,4,5],[7,6,4,3,1],[]]
    ans = [7,4,0,0]
    s = Solution()
    for i,t in enumerate(tc):
        if(s.maxProfit(t) != ans[i]): print("incorrect: ",i,t)

