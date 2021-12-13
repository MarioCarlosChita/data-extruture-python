class Solution(object):
    def containsDuplicate(self, nums):
        self.list = {}
        for v in nums:
            if v not in self.list:
                self.list[v] = [v]
            else:
                return True
        return False
