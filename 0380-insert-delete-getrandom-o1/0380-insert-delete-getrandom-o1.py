import random

class RandomizedSet(object):

    def __init__(self):
      self.mySet=set()

    def insert(self, val):
        if val in self.mySet:
            return False
        self.mySet.add(val)
        return True
        
        """
        :type val: int
        :rtype: bool
        """
        

    def remove(self, val):
        if val in self.mySet:
            self.mySet.remove(val)
            return True
        return False
        """
        :type val: int
        :rtype: bool
        """
        

    def getRandom(self):
        if not self.mySet:
            return None
        return random.choice(list(self.mySet))
        """
        :rtype: int
        """
        

