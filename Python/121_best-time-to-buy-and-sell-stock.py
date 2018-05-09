""" 
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

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
        # Approach #2, find bottom and top
        # keep bottom and maximumProfit. Whenever any prices is lower than bottom, bottom is updated
        # keep searching maximumProfit until list end.
        # O(n),36%, 50ms
        bottom = 0
        maxPro = 0
        for i in range(1,len(prices)):
            if prices[i] < prices[bottom]:
                bottom = i
            else:
                maxPro = max(maxPro, prices[i] - prices[bottom])
        return maxPro

    def maxProfit2(self, prices):
        # Approach #1, brute force.
        # Search every possible i, j, where i>j and prices[j] - [i] is maximum
        # nested loop
        # O(n^2)
        # Time limit exceeded
        maximum = 0
        for i in range(len(prices)):
            for j in range(i,len(prices)):
                maximum = max(maximum, prices[j]-prices[i])
        return maximum
        
        


if __name__ == "__main__":
    tc = [[7,1,5,3,6,4],[7,6,4,3,1]]
    s = Solution()
    for t in tc:
        print(t)
        print(s.maxProfit(t))

