class Solution(object):
    def rotate(self,nums, k):
      n=len(nums)
      k%=n
      def rev(start, end):
          while start < end:
              nums[start], nums[end] = nums[end], nums[start]
              start += 1
              end -= 1

      rev(0,n-1)
      rev(0,k-1)
      rev(k,n-1)

      return nums  
