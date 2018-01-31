"""
Topic: 
    Best Time to Buy and Sell Stock
Description:
    Say you have an array for which the ith element is the price of a given stock on day i.
    If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), 
    design an algorithm to find the maximum profit.
"""
class Solution:
    """
    :type prices: List[int]
    :rtype: int
    """
    # Solution 1: Use a variable to record minimum price and calculate the maximum profit value.
    # Testcase Runtime: 77ms
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def maxProfit(self, prices):

        min_price, max_profit = float('inf'), 0
        for price in prices:
            if price < min_price:
                min_price = price
            elif price-min_price > max_profit:
                max_profit = price-min_price    
        return max_profit