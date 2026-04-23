class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        curr_lowest = float('inf')
        for price in prices:
            if price < curr_lowest:
                curr_lowest = price
            else:
                profit = price - curr_lowest
                if profit>max_profit:
                    max_profit = profit
        return max_profit