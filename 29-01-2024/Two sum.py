class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i,n in enumerate(nums):
            complement = target - n
            if complement in hashmap:
                return [hashmap[complement],i]
            hashmap[n] = i
