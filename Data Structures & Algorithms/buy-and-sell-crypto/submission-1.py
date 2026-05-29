class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if sorted(prices,reverse=True) == prices:
            return 0

        profit = 0
        l = 0
        r = 1

        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
            else:
                profit = max(profit, prices[r]-prices[l])
            r += 1
        return profit