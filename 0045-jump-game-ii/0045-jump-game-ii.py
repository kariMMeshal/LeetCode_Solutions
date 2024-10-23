
# Greedy Algorithm
class Solution(object):

  def jump(self,nums):

    jumps = 0
    farthest=0
    currentEnd=0
    for i in range(len(nums) - 1):
      farthest = max(farthest , i+nums[i]) 
      print(farthest  , currentEnd , i)
      if i ==currentEnd :
          jumps+=1
          currentEnd=farthest
      if currentEnd >= len(nums)-1:
          break
    return jumps      
    