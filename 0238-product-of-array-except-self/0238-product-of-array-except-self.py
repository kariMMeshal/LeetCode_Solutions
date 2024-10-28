# prefix_product + suffix_Product = Product without the index
class Solution(object):
    def productExceptSelf(self,nums):
      output = [0]*len(nums)
      left_product = 1
      right_product = 1
      # [1,2,3,4] , [1,1,2,6]
      for i in range(len(nums)):
        output[i]=left_product
        left_product*=nums[i]
      print(output)
      # [1,2,3,4]  , [1,1,2,6]
      for j in range(len(nums)-1,-1,-1):
        output[j]*=right_product
        right_product*=nums[j]
      print(output)
      return output   
