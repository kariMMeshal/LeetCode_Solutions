
def findPivot(citations , start , end):

    pivot = citations[end]
    i=start-1
    for j in range(start,end):
        if(citations[j]>pivot):
            i+=1
            citations[i],citations[j] = citations[j] , citations[i]
    i+=1
    citations[i] , citations[end] = citations[end],citations[i] 
    
    return i   #  the new pivot
        

                      # 0      7
def quickSort(citations,start,end):
    if(end<=start):
        return 
    pivot = findPivot(citations , start , end)
    quickSort(citations , start , pivot-1)
    quickSort(citations , pivot+1 , end)
    
    

  
class Solution(object):

    def hIndex(self,citations):

        """
        :type citations: List[int]
        :rtype: int
        """
        quickSort(citations,0,len(citations)-1)
        h=0
        for n in citations:
            if(n>h):
                h+=1
        return h
        
