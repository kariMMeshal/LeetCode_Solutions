class Solution(object):
    def canJump(self,nums):
        jumbs = 0
        for n in nums:
            if jumbs < 0:
                return False
            elif n > jumbs:
                jumbs = n
            jumbs -= 1
        return True