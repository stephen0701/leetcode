"""
Topic: 
    Best Time to Buy and Sell Stock II
Description:
    Say you have an array for which the ith element is the price of a given stock on day i.
    Design an algorithm to find the maximum profit. 
    You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). 
    However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""

class Solution:
    """
    :type prices: List[int]
    :rtype: int
    """
    # Solution: Accumulate the profit each time when the price is going upwards.
    # Testcase Runtime: 73ms
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def maxProfit(self, prices):
        profit = 0
        for i in range(len(prices)):
            if i > 0 and prices[i]>prices[i-1]:
                profit += prices[i]-prices[i-1]
        return profit