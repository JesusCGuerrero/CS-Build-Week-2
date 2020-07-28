class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numsSet = set(nums)
        if len(nums) != len(numsSet):
            return True
        else:
            return False