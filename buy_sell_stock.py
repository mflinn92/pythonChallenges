
#Say you have an array for which the ith element is the price of a given stock on day i.

#Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

#You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
#After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)

def maxProfit(prices: List[int]) -> int:
    #case1 
    #we can have a stock
    #results from either selling or doing nothing
    #case 2 we can have no stock
    # 
    #case 3 we can be in cooldown

    have_stock_profit = float("-inf")
    no_stock_profit, cooldown_profit = 0, 0

    for price in prices:
        temp = no_stock_profit
        no_stock_profit = max(no_stock_profit, have_stock_profit + price)
        have_stock_profit = max(have_stock_profit, cooldown_profit - price)
        cooldown_profit = max(cooldown_profit, temp)
    return max(cooldown_profit, no_stock_profit) 

