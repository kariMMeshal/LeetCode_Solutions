

class Solution(object):
    def removeDuplicates(self,nums):
        k=1
        for i in range(1,len(nums)):
            if(nums[i] !=nums[k-1]):
                nums[k]=nums[i]
                k+=1
        del nums[k:]        
        return k        