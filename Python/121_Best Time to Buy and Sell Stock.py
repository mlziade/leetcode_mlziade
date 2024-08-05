class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        more_profitable_transaction = [0,0]
        cheaper = 0
        most_expensive = 0
        for i, price in enumerate(prices):
            if price < prices[cheaper]:
                cheaper = i
                most_expensive = i
            if price > prices[most_expensive]:
                most_expensive = i
            if most_expensive > cheaper and (prices[more_profitable_transaction[1]] - prices[more_profitable_transaction[0]]) < (prices[most_expensive] - prices[cheaper]):
                more_profitable_transaction = [cheaper, most_expensive]
            """ print(prices)
            print(more_profitable_transaction)
            print(cheaper, most_expensive)
            print("-----------------------") """
        sum_of_more_profitable_transaction = prices[more_profitable_transaction[1]] - prices[more_profitable_transaction[0]]
        return sum_of_more_profitable_transaction
            