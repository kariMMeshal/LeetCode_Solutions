
class Solution(object):
    def maxProfit(self , prices):
      minPrice=prices[0]
      maxProfit=0
      for i in range(len(prices)):
        if(prices[i] <  minPrice ):
          minPrice=prices[i]
        if(prices[i]-minPrice> maxProfit):
          maxProfit=prices[i]-minPrice
      return maxProfit    