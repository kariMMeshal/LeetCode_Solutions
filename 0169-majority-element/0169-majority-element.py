
class Solution(object):
    def majorityElement(self,nums):
        candidate = nums[0] 
        count=1           
        # print(len(nums) // 2)
        for i in range(1,len(nums)) :
            if(candidate!=nums[i]):
                count-=1
                if(count == 0 ):
                    candidate =nums[i]
                    count+=1
            else :
                count+=1        
        return candidate            
            
