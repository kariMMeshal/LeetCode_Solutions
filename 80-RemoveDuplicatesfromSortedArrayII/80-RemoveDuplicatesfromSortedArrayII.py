
class Solution(object):
    def removeDuplicates(self , nums):

        element_count = collections.Counter()
        k=0

        for i in range(len(nums)):
          if( element_count[nums[i]] <2 ):
            nums[k]=nums[i]
            k+=1
            element_count[nums[i]]+=1
        del nums[k:]    

        return k
