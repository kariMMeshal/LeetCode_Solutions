
class Solution(object):
    def maxProfit(self, prices):
      maxProfit=0
      for i in range(len(prices)-1):
        profit=prices[i+1]-prices[i] 
        if(profit > 0):
          maxProfit+=profit

      return maxProfit    